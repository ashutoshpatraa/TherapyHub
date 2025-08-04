# TherapyHub 🧠💚

**Anonymous Peer Support Platform for Mental Health**

Created by [ashutoshpatraa](https://github.com/ashutoshpatraa)

A Flask-based web application providing a safe, anonymous space for mental health peer support with AI-powered sentiment analysis and content moderation.

## 🚀 Quick Start

**Ultra-Simple Setup - Just One Command:**

```bash
python app.py
```

**First Time Setup:**
```bash
# Clone repository
git clone https://github.com/ashutoshpatraa/TherapyHub.git
cd TherapyHub

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

**Everything happens automatically:**
- ✅ Creates SQLite database (`therapyhub.db`)
- ✅ Downloads NLTK data if needed
- ✅ Creates admin user (admin/admin123)
- ✅ Starts web server at `http://localhost:5000`

## ✨ Features

### 🎨 **Beautiful, Warm UI Design**
- **Emotional Color Palette** - Warm pinks, gentle purples, calming blues
- **Friendly Typography** - Nunito font for warmth and readability
- **Smooth Animations** - Floating elements, hover effects, gentle transitions
- **Accessible Design** - High contrast, keyboard navigation, ARIA labels
- **Mobile-First** - Responsive design that works on all devices

### 🧠 **Mental Health Focused**
- **Anonymous Posting** - Share feelings with complete privacy protection
- **AI Sentiment Analysis** - Automatic emotion detection using TextBlob/NLTK
- **Smart Content Safety** - Real-time toxic content filtering and moderation
- **Personalized Resources** - AI-generated coping strategies based on emotions
- **Peer Support System** - Community members provide encouragement and support
- **Crisis Resources** - Emergency contact information prominently displayed

### 🛡️ **Safety & Moderation**
- **AI-Powered Moderation** - Automatic detection of harmful content
- **Admin Dashboard** - Human oversight for flagged content review
- **Emotion Categorization** - Posts sorted by: Positive, Sad, Anxious, Stressed
- **Content Guidelines** - Clear community standards and expectations

## 🛠️ Tech Stack

### **Frontend Design**
- **UI Framework**: Custom CSS with warm, mental-health focused design
- **Typography**: Nunito & Inter fonts for emotional warmth and readability
- **Color Psychology**: Carefully chosen colors (warm pinks, calming blues, healing greens)
- **Animations**: CSS transitions, floating elements, smooth hover effects
- **Responsive**: Mobile-first design with Bootstrap 5 grid system
- **Accessibility**: ARIA labels, keyboard navigation, high contrast ratios

### **Backend & AI**
- **Framework**: Python Flask with SQLAlchemy ORM
- **Database**: SQLite (zero-configuration, perfect for development)
- **AI/NLP**: TextBlob + NLTK for sentiment analysis and emotion detection
- **Security**: Werkzeug password hashing + Flask-Login session management
- **Content Safety**: Custom toxic keyword filtering with AI sentiment analysis

## 📱 How It Works

1. **Register/Login** → Create anonymous account
2. **Share Feelings** → Post about emotional state
3. **AI Analysis** → System analyzes sentiment & categorizes emotions
4. **Get Resources** → Receive personalized calming strategies
5. **Community Support** → Others reply with encouragement
6. **Content Safety** → Toxic replies automatically flagged

## 🎯 Admin Access

**Username**: `admin` | **Password**: `admin123`  
**Admin Panel**: `http://localhost:5000/admin/flagged`

## 📁 Project Structure

```
TherapyHub/
├── app.py              ← 🎯 Main application (just run this!)
├── requirements.txt    ← Python dependencies
├── README.md          ← This documentation
├── templates/         ← HTML templates (9 files)
└── therapyhub.db      ← SQLite database (auto-created)
```

## 🔧 Key Routes

- `/` - Home page
- `/register` `/login` - Authentication
- `/posts` - Community feed
- `/create_post` - Share feelings
- `/post/<id>` - View post with replies
- `/reply/<post_id>` - Reply to posts
- `/admin/flagged` - Admin moderation panel

## 🧠 AI Features

**Sentiment Analysis:**
- Analyzes emotional polarity (-1 to 1)
- Categorizes emotions: Stressed, Anxious, Sad, Positive, Neutral
- Keyword detection for emotion-specific terms

**Content Safety:**
- Toxic keyword filtering with predefined blacklist
- Auto-flags replies with very negative sentiment
- Manual admin review system for flagged content

**Calming Resources:**
- **Stressed**: Breathing exercises, relaxation techniques
- **Anxious**: Grounding techniques, mindfulness exercises
- **Sad**: Social connection suggestions, self-care activities

## ⚙️ Configuration (Optional)

**Environment Variables (.env):**
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///therapyhub.db
```

**Custom Content Filtering:**
Edit `TOXIC_KEYWORDS` list in `app.py` to customize content filtering.

## 🚨 Important Notices

**Mental Health Disclaimer:**
- Provides **peer support only** - not professional therapy
- Crisis situations should contact emergency services
- Emergency: 911 | Crisis Text: HOME to 741741 | Suicide Prevention: 988

**Security:**
- Change admin credentials in production
- Update SECRET_KEY for production use
- Implement HTTPS for production deployment

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Make changes
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details.

## 👨‍💻 Developer

**Created by:** [Ashutosh Patra](https://github.com/ashutoshpatraa)  
**Repository:** [TherapyHub](https://github.com/ashutoshpatraa/TherapyHub)  
**Issues:** [GitHub Issues](https://github.com/ashutoshpatraa/TherapyHub/issues)

---

**⭐ If this project helped you, please give it a star on GitHub!**

*Remember: TherapyHub provides peer support - always encourage professional help for serious mental health concerns.*
