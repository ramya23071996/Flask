from app import create_app, db
import os


app = create_app()
app.app_context().push()  # sets current context
db.create_all()           # creates the database tables



class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
