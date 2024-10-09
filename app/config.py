from datetime import timedelta
import os

class Config:
    SECRET_KEY = '' # your secret key here
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__)) + '/uploads'
    TEMPLATES_FOLDER = os.path.abspath(os.path.dirname(__file__)) + '/templates'
    STATIC_FOLDER = os.path.abspath(os.path.dirname(__file__)) + '/static'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')