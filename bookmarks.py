from flask import Flask, redirect, render_template, url_for
from bookform import Bookmarks
# from bookmodels import BookmarksModel
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1ecc4ba444d91d97d0da200bdde1da7'  #To protect from attacks  python -m secrets  "secrets.token_hex(16)"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///book.db'   #use Sqlite location for SQLAlchemy
db = SQLAlchemy(app)  ##Instantiate DB, python > from app import db, db.create_all()

@app.route("/", methods=['GET', 'POST'])
# @app.route("/book", methods=['GET', 'POST'])
def home():
    data = BookmarksModel.query.all()
    return render_template('book.html', title='list of Bookmarks', form=data)

@app.route("/book/", methods=['GET', 'POST'])
# @app.route("/book/<int:id>/update", methods=['GET', 'POST'])
# def bookedit(id):
def bookedit1():
    form=Bookmarks()
    if form.is_submitted():
        rec=BookmarksModel(category=form.category.data, details=form.details.data)
        db.session.add(rec)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('bookedit.html', title='Add bookmarks', form=form)

@app.route("/book/<int:id>/update", methods=['GET', 'POST'])
def bookedit(id):
    form=Bookmarks()
    rec=BookmarksModel.query.get_or_404(id)
    if form.is_submitted():
        rec.category=form.category.data
        rec.details=form.details.data
        rec.id=id
        db.session.commit()
        return redirect(url_for('home'))
    else:        
        form.details.data=rec.details
        form.category.data=rec.category
        form.id.data = id
        return render_template('bookedit.html', title='Add bookmarks', form=form)

class BookmarksModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), unique=False, nullable=False)
    details = db.Column(db.String(40), unique=False, nullable=False)
    inserttime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

if __name__ == '__main__':
    app.run(debug=True)