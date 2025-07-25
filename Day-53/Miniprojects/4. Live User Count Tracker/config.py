import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    pass