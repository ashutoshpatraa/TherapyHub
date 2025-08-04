#!/usr/bin/env python3
"""
TherapyHub - Anonymous Peer Support Platform

🚀 ULTRA-SIMPLE SETUP: Just run this file!
   python app.py

✅ Everything included:
   - Flask web application
   - SQLite database (auto-created)
   - Sentiment analysis (TextBlob + NLTK)
   - User authentication & admin panel
   - Content moderation & safety features
   - Bootstrap UI templates

🌐 Access: http://localhost:5000
👤 Admin: username=admin, password=admin123

No configuration files, no database setup, no batch scripts needed!
"""

import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from textblob import TextBlob
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///therapyhub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Blacklist for toxic content
TOXIC_KEYWORDS = [
    'kill yourself', 'kys', 'suicide', 'die', 'harm yourself', 'hurt yourself',
    'worthless', 'loser', 'pathetic', 'stupid', 'idiot', 'hate you', 'disgusting'
]

# Calming resources
CALMING_RESOURCES = {
    'stressed': [
        "Try deep breathing: Inhale for 4 counts, hold for 4, exhale for 4.",
        "Take a short walk or do some light stretching.",
        "Listen to calming music or nature sounds."
    ],
    'anxious': [
        "Ground yourself: Name 5 things you can see, 4 you can touch, 3 you can hear.",
        "Practice progressive muscle relaxation.",
        "Try meditation or mindfulness exercises."
    ],
    'sad': [
        "Reach out to a trusted friend or family member.",
        "Engage in activities you enjoy or find meaningful.",
        "Consider journaling about your feelings."
    ]
}

# Models
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    anonymous_name = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    replies = db.relationship('Reply', backref='author', lazy=True)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
    emotion_category = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    replies = db.relationship('Reply', backref='post', lazy=True, cascade='all, delete-orphan')

class Reply(db.Model):
    __tablename__ = 'replies'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reply_text = db.Column(db.Text, nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
    flagged = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Forms
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    anonymous_name = StringField(validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Anonymous Display Name"})
    password = PasswordField(validators=[InputRequired(), Length(min=6, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user = User.query.filter_by(username=username.data).first()
        if existing_user:
            raise ValidationError('Username already exists. Choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=6, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    content = TextAreaField(validators=[InputRequired(), Length(min=10, max=1000)], render_kw={"placeholder": "Share your thoughts...", "rows": 4})
    submit = SubmitField('Post')

class ReplyForm(FlaskForm):
    reply_text = TextAreaField(validators=[InputRequired(), Length(min=5, max=500)], render_kw={"placeholder": "Write a supportive reply...", "rows": 3})
    submit = SubmitField('Reply')

# Sentiment Analysis Functions
def analyze_sentiment(text):
    """Analyze sentiment using TextBlob"""
    blob = TextBlob(text)
    return blob.sentiment.polarity

def categorize_emotion(text, sentiment_score):
    """Categorize emotion based on text content and sentiment"""
    text_lower = text.lower()
    
    stress_words = ['stress', 'stressed', 'overwhelmed', 'pressure', 'deadline', 'work', 'busy']
    anxiety_words = ['anxious', 'anxiety', 'worry', 'worried', 'nervous', 'panic', 'fear', 'scared']
    sad_words = ['sad', 'depressed', 'down', 'lonely', 'empty', 'hopeless', 'cry', 'crying']
    
    if any(word in text_lower for word in stress_words):
        return 'stressed'
    elif any(word in text_lower for word in anxiety_words):
        return 'anxious'
    elif any(word in text_lower for word in sad_words) or sentiment_score < -0.3:
        return 'sad'
    elif sentiment_score > 0.3:
        return 'positive'
    else:
        return 'neutral'

def is_toxic_content(text):
    """Check if text contains toxic keywords"""
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in TOXIC_KEYWORDS)

def should_flag_reply(text, sentiment_score):
    """Determine if a reply should be flagged"""
    return is_toxic_content(text) or sentiment_score < -0.7

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data,
            anonymous_name=form.anonymous_name.data,
            password_hash=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('posts'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    
    if form.validate_on_submit():
        sentiment_score = analyze_sentiment(form.content.data)
        emotion_category = categorize_emotion(form.content.data, sentiment_score)
        
        new_post = Post(
            user_id=current_user.id,
            content=form.content.data,
            sentiment_score=sentiment_score,
            emotion_category=emotion_category
        )
        db.session.add(new_post)
        db.session.commit()
        
        flash('Your post has been created!')
        return redirect(url_for('posts'))
    
    return render_template('create_post.html', form=form)

@app.route('/posts')
def posts():
    all_posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('posts.html', posts=all_posts)

@app.route('/post/<int:id>')
def view_post(id):
    post = Post.query.get_or_404(id)
    replies = Reply.query.filter_by(post_id=id).filter_by(flagged=False).order_by(Reply.created_at.asc()).all()
    
    # Get calming resources if the post indicates negative emotions
    resources = []
    if post.emotion_category in CALMING_RESOURCES:
        resources = CALMING_RESOURCES[post.emotion_category]
    
    return render_template('view_post.html', post=post, replies=replies, resources=resources)

@app.route('/reply/<int:post_id>', methods=['GET', 'POST'])
@login_required
def reply_to_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = ReplyForm()
    
    if form.validate_on_submit():
        sentiment_score = analyze_sentiment(form.reply_text.data)
        flagged = should_flag_reply(form.reply_text.data, sentiment_score)
        
        if flagged:
            flash('Your reply contains inappropriate content and has been flagged for review.')
        
        new_reply = Reply(
            post_id=post_id,
            user_id=current_user.id,
            reply_text=form.reply_text.data,
            sentiment_score=sentiment_score,
            flagged=flagged
        )
        db.session.add(new_reply)
        db.session.commit()
        
        if not flagged:
            flash('Your reply has been posted!')
        
        return redirect(url_for('view_post', id=post_id))
    
    return render_template('reply.html', form=form, post=post)

@app.route('/admin/flagged')
@login_required
def admin_flagged():
    # Simple admin check - in production, implement proper admin roles
    if current_user.username != 'admin':
        flash('Access denied. Admin privileges required.')
        return redirect(url_for('posts'))
    
    flagged_replies = Reply.query.filter_by(flagged=True).order_by(Reply.created_at.desc()).all()
    return render_template('admin_flagged.html', replies=flagged_replies)

@app.route('/admin/approve_reply/<int:reply_id>')
@login_required
def approve_reply(reply_id):
    if current_user.username != 'admin':
        flash('Access denied.')
        return redirect(url_for('posts'))
    
    reply = Reply.query.get_or_404(reply_id)
    reply.flagged = False
    db.session.commit()
    flash('Reply approved!')
    return redirect(url_for('admin_flagged'))

@app.route('/admin/delete_reply/<int:reply_id>')
@login_required
def delete_reply(reply_id):
    if current_user.username != 'admin':
        flash('Access denied.')
        return redirect(url_for('posts'))
    
    reply = Reply.query.get_or_404(reply_id)
    db.session.delete(reply)
    db.session.commit()
    flash('Reply deleted!')
    return redirect(url_for('admin_flagged'))

def create_admin_user():
    """Create admin user if it doesn't exist"""
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin_user = User(
            username='admin',
            anonymous_name='TherapyHub Admin',
            password_hash=generate_password_hash('admin123')
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")
        print("Username: admin")
        print("Password: admin123")
    else:
        print("Admin user already exists.")

def initialize_app():
    """Initialize the application and database"""
    try:
        # Download NLTK data if needed
        import nltk
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            print("Downloading NLTK data...")
            nltk.download('punkt')
            nltk.download('brown')
            print("NLTK data downloaded successfully!")
        
        # Create database tables
        with app.app_context():
            db.create_all()
            print("Database tables created successfully!")
            create_admin_user()
            
    except Exception as e:
        print(f"Error initializing application: {e}")
        return False
    return True

if __name__ == '__main__':
    print("=" * 50)
    print("TherapyHub - Anonymous Peer Support Platform")
    print("=" * 50)
    
    # Initialize application
    if initialize_app():
        print("\nStarting TherapyHub...")
        print("Access the application at: http://localhost:5000")
        print("Admin panel: http://localhost:5000/admin/flagged")
        print("Press Ctrl+C to stop the server")
        print("=" * 50)
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("Failed to initialize application.")
        exit(1)
