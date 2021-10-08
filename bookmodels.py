from datetime import datetime
from app import db


class BookmarksModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), unique=False, nullable=False)
    details = db.Column(db.String(40), unique=False, nullable=False)
    inserttime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

