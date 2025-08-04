-- Create database and tables for TherapyHub
CREATE DATABASE IF NOT EXISTS therapyhub;
USE therapyhub;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(80) UNIQUE NOT NULL,
    anonymous_name VARCHAR(80) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Posts table
CREATE TABLE IF NOT EXISTS posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    sentiment_score FLOAT NOT NULL,
    emotion_category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Replies table
CREATE TABLE IF NOT EXISTS replies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    reply_text TEXT NOT NULL,
    sentiment_score FLOAT NOT NULL,
    flagged BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create admin user (password: admin123)
INSERT INTO users (username, anonymous_name, password_hash) 
VALUES ('admin', 'TherapyHub Admin', 'scrypt:32768:8:1$gqV9JgqOt8OjGBGY$46267e81c93a0f2c2e9c1a7a8b3d4e5f6789a0b1c2d3e4f567890abcdef123456789abcdef0123456789abcdef0123456789abcdef')
ON DUPLICATE KEY UPDATE username=username;
