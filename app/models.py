from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Model

class ShortLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True)
    short_url = db.Column(db.String(6), unique=True)