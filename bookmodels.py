from datetime import datetime
from app import db




class Bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(80), unique=True)
    details = db.Column(db.String(120), unique=True)
    url = db.Column(db.String(120), unique=True)
    inserttime = db.column(db.DateTime)
    def __init__(self, Bookmarksname, email):
        self.catagory = catagory
        self.details = details
    def __repr__(self):
        return '<Bookmarks %r>' % self.details
