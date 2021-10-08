from flask import Flask, redirect, render_template, url_for, request
from bookform import BookmarksForm
# from bookmodels import BookmarksModel
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1ecc4ba444d91d97d0da200bdde1da7'  #To protect from attacks  python -m secrets  "secrets.token_hex(16)"
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///book.db'   #use Sqlite location for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://operator:tej1nder@192.168.0.172:3306/Server' ##MariaDB entry
db = SQLAlchemy(app)  ##Instantiate DB, python > from app import db, db.create_all()

@app.route("/", methods=['GET', 'POST'])
# @app.route("/book", methods=['GET', 'POST'])
def home():
    # data = Bookmarks.query.all()   ## removed for paginating
    page = request.args.get('page', 1, type=int)
    data = Bookmarks.query.paginate(page=page) #Start paginating
    return render_template('book.html', title='list of Bookmarks', form=data)

@app.route("/book/", methods=['GET', 'POST'])
# @app.route("/book/<int:id>/update", methods=['GET', 'POST'])
# def bookedit(id):
def bookedit1():
    form=BookmarksForm()
    if form.is_submitted():
        rec=BookmarksModel(catagory=form.catagory.data, details=form.details.data, url=form.url.data)
        db.session.add(rec)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('bookedit.html', title='Add bookmarks', form=form)

@app.route("/book/<int:id>/update", methods=['GET', 'POST'])
def bookedit(id):
    form=BookmarksForm()
    rec=Bookmarks.query.get_or_404(id)
    if form.is_submitted():
        rec.catagory=form.catagory.data
        rec.details=form.details.data
        rec.id=id
        rec.url = form.url.data
        db.session.commit()
        return redirect(url_for('home'))
    else:        
        form.details.data=rec.details
        form.catagory.data=rec.catagory
        form.id.data = id
        form.url.data = rec.url
        return render_template('bookedit.html', title='Add bookmarks', form=form)

class Bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(40), unique=False, nullable=False)
    details = db.Column(db.String(100), unique=False, nullable=False)
    inserttime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    url = db.Column(db.String(120), unique=True)
    def __init__(self, Bookmarksname, email):
        self.catagory = catagory
        self.details = details
    def __repr__(self):
        return '<Bookmarks %r>' % self.details    

if __name__ == '__main__':
    app.run(debug=True)