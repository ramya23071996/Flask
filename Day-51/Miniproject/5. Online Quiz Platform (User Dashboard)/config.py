import os

class Config:
    SECRET_KEY = 'your-secret-key'  # Replace with a secure random key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False