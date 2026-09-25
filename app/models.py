from app import db
from datetime import datetime

class Teste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=True, default=datetime.utcnow())
    email = db.Column(db.Integer, nullable=True)
    senha= db.Column(db.Integer, nullable=True)