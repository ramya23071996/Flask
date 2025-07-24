import os

class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/note_app.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
