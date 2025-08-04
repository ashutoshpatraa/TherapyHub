# TherapyHub Configuration Guide

## Database Configuration

### SQLite (Default - No Setup Required!)
The application uses SQLite by default, which requires no installation or configuration:
- Database file: `therapyhub.db` (created automatically)
- Connection string: `sqlite:///therapyhub.db`
- Perfect for development and small deployments

### Alternative Database Options (Advanced)

#### Option 1: MySQL
If you prefer MySQL:
1. Install MySQL Server
2. Create database: `CREATE DATABASE therapyhub;`
3. Update connection string in app.py:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/therapyhub'
   ```
4. Install PyMySQL: `pip install PyMySQL`

#### Option 2: PostgreSQL
For PostgreSQL:
1. Install PostgreSQL
2. Create database
3. Update connection string:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/therapyhub'
   ```
4. Install psycopg2: `pip install psycopg2-binary`

## Environment Variables

Create a `.env` file in the project root:
```env
SECRET_KEY=your-very-secret-key-here
DATABASE_URL=sqlite:///therapyhub.db
FLASK_ENV=development
FLASK_DEBUG=True
```

## Security Notes

### For Production:
- Change the SECRET_KEY to a strong, random value
- Set FLASK_DEBUG=False
- Use environment variables for sensitive data
- Implement HTTPS
- Set up proper logging
- Use a production WSGI server like Gunicorn

### Default Admin Account:
- Username: admin
- Password: admin123
- **IMPORTANT**: Change this password immediately in production!

## Troubleshooting

### Common Issues:
1. **ModuleNotFoundError**: Make sure virtual environment is activated
2. **Database Connection Error**: Check MySQL is running and credentials are correct
3. **NLTK Data Missing**: Run `python setup_nltk.py`
4. **Permission Errors**: Run as administrator or check file permissions

### Testing the Application:
1. Run `python app.py`
2. Open http://localhost:5000
3. Register a new account
4. Create a test post
5. Check sentiment analysis is working
6. Test the admin panel at http://localhost:5000/admin/flagged

**No database setup required!** SQLite database is created automatically.
