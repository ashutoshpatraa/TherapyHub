#!/usr/bin/env python3
"""
TherapyHub Startup Script
This script initializes the database and runs the Flask application
"""

import os
import sys
from app import app, db
from werkzeug.security import generate_password_hash

def create_admin_user():
    """Create admin user if it doesn't exist"""
    from app import User
    
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

def initialize_database():
    """Initialize the database with tables"""
    try:
        with app.app_context():
            # Create all tables
            db.create_all()
            print("Database tables created successfully!")
            
            # Create admin user
            create_admin_user()
            
    except Exception as e:
        print(f"Error initializing database: {e}")
        return False
    return True

def run_app():
    """Run the Flask application"""
    print("Starting TherapyHub...")
    print("Access the application at: http://localhost:5000")
    print("Admin panel: http://localhost:5000/admin/flagged")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    print("=" * 50)
    print("TherapyHub - Anonymous Peer Support Platform")
    print("=" * 50)
    
    # Initialize database
    if initialize_database():
        print("\nStarting application...")
        run_app()
    else:
        print("Failed to initialize database. Please check your MySQL connection.")
        sys.exit(1)
