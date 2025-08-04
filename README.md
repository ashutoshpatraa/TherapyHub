# TherapyHub 🧠💚

**Anonymous Peer Support Platform for Mental Health**

TherapyHub is a Flask-based web application that provides a safe, anonymous space for mental health peer support. Users can share their feelings, receive supportive responses, and access helpful resources through an AI-powered sentiment analysis system.

## 🚀 Features

### Core Functionality
- **Anonymous Posting**: Share feelings and experiences with complete anonymity
- **Peer Support**: Community members can reply with supportive messages
- **Sentiment Analysis**: AI-powered emotion detection using TextBlob/NLTK
- **Content Safety**: Automatic flagging of toxic or harmful content
- **Calming Resources**: Personalized coping strategies based on detected emotions
- **Admin Moderation**: Simple admin panel for content review

### Technical Features
- **Backend**: Python Flask with SQLAlchemy ORM
- **Database**: MySQL with PyMySQL connector
- **NLP**: TextBlob for sentiment analysis and emotion categorization
- **Frontend**: Bootstrap 5 responsive design
- **Security**: Password hashing with Werkzeug
- **Authentication**: Flask-Login for session management

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package manager)

### 1. Clone Repository
```bash
git clone <repository-url>
cd TherapyHub
```

### 2. Set Up Python Environment
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup
1. **Start MySQL Server**
2. **Create Database** (Optional - can be done automatically):
   ```sql
   CREATE DATABASE therapyhub;
   ```
3. **Update Database Configuration** in `app.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/therapyhub'
   ```

### 4. Initialize NLTK Data
```powershell
python setup_nltk.py
```

### 5. Run Application
```powershell
python run.py
```

The application will be available at: `http://localhost:5000`

## 🗄️ Database Schema

### Users Table
```sql
- id (INT, PRIMARY KEY)
- username (VARCHAR(80), UNIQUE)
- anonymous_name (VARCHAR(80))
- password_hash (VARCHAR(255))
- created_at (TIMESTAMP)
```

### Posts Table
```sql
- id (INT, PRIMARY KEY)
- user_id (INT, FOREIGN KEY)
- content (TEXT)
- sentiment_score (FLOAT)
- emotion_category (VARCHAR(50))
- created_at (TIMESTAMP)
```

### Replies Table
```sql
- id (INT, PRIMARY KEY)
- post_id (INT, FOREIGN KEY)
- user_id (INT, FOREIGN KEY)
- reply_text (TEXT)
- sentiment_score (FLOAT)
- flagged (BOOLEAN)
- created_at (TIMESTAMP)
```

## 🛣️ API Routes

### Authentication
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET /logout` - User logout

### Core Features
- `GET /` - Home page
- `GET /posts` - Community feed
- `GET/POST /create_post` - Create new post
- `GET /post/<id>` - View specific post with replies
- `GET/POST /reply/<post_id>` - Reply to a post

### Admin Panel
- `GET /admin/flagged` - View flagged content
- `GET /admin/approve_reply/<id>` - Approve flagged reply
- `GET /admin/delete_reply/<id>` - Delete flagged reply

## 🧠 AI Features

### Sentiment Analysis
- **TextBlob Integration**: Analyzes emotional polarity (-1 to 1)
- **Emotion Categorization**: Stressed, Anxious, Sad, Positive, Neutral
- **Keyword Detection**: Identifies emotion-specific terms

### Content Safety
- **Toxic Keyword Filtering**: Predefined blacklist of harmful terms
- **Negative Sentiment Flagging**: Auto-flags replies with very negative scores
- **Admin Review System**: Manual approval for flagged content

### Calming Resources
Personalized suggestions based on detected emotions:
- **Stressed**: Breathing exercises, relaxation techniques
- **Anxious**: Grounding techniques, mindfulness exercises  
- **Sad**: Social connection suggestions, self-care activities

## 👤 Default Admin Account

**Username**: `admin`  
**Password**: `admin123`  
**Access**: `http://localhost:5000/admin/flagged`

*⚠️ Change admin credentials in production!*

## 🔧 Configuration

### Environment Variables (.env)
```env
SECRET_KEY=your-secret-key-change-this-in-production
DATABASE_URL=mysql+pymysql://root:password@localhost/therapyhub
FLASK_ENV=development
FLASK_DEBUG=True
```

### Content Filtering
Modify `TOXIC_KEYWORDS` list in `app.py` to customize content filtering:
```python
TOXIC_KEYWORDS = [
    'kill yourself', 'kys', 'suicide', 'die', 
    'harm yourself', 'hurt yourself', 'worthless'
    # Add more keywords as needed
]
```

## 🚨 Important Notes

### Mental Health Disclaimer
- This platform provides **peer support only**
- **Not a substitute** for professional mental health care
- Emergency contacts provided on homepage
- Crisis situations should contact emergency services

### Security Considerations
- Change default admin credentials
- Update SECRET_KEY in production
- Use environment variables for sensitive config
- Implement HTTPS in production
- Regular security audits recommended

## 🛠️ Development

### Project Structure
```
TherapyHub/
├── app.py                 # Main Flask application
├── run.py                 # Startup script
├── requirements.txt       # Python dependencies
├── setup_nltk.py         # NLTK data downloader
├── database_setup.sql    # MySQL schema
├── .env                  # Environment variables
└── templates/            # HTML templates
    ├── base.html
    ├── home.html
    ├── register.html
    ├── login.html
    ├── create_post.html
    ├── posts.html
    ├── view_post.html
    ├── reply.html
    └── admin_flagged.html
```

### Adding New Features
1. **New Routes**: Add to `app.py`
2. **Database Changes**: Update models and run migrations
3. **Templates**: Create/modify HTML files in `templates/`
4. **Sentiment Features**: Extend emotion categorization logic
5. **Admin Features**: Add to admin panel routes

## 📱 Usage Examples

### Creating a Post
1. Register/Login to account
2. Click "Share Your Feelings"
3. Write about your current emotional state
4. System analyzes sentiment and categorizes emotion
5. Receive relevant calming resources if needed

### Replying with Support
1. Browse community feed
2. Click "View & Reply" on a post
3. Write supportive, encouraging message
4. System checks for toxic content
5. Reply posted if approved, flagged if problematic

### Admin Moderation
1. Login as admin user
2. Visit `/admin/flagged`
3. Review flagged replies
4. Approve appropriate content
5. Delete harmful/inappropriate replies

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Implement changes with tests
4. Update documentation
5. Submit pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support & Resources

### Crisis Resources
- **Emergency**: 911 (US) or local emergency services
- **Crisis Text Line**: Text HOME to 741741
- **National Suicide Prevention Lifeline**: 988
- **International**: Visit findahelpline.com

### Technical Support
- Create issue on GitHub repository
- Check documentation and README
- Review error logs in console

---

**Remember**: TherapyHub is a peer support platform. Always encourage professional help for serious mental health concerns.TherapyHub
” anonymous peer support platform using Python, Flask, and MySQL.
