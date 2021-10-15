from flask import Flask, redirect, render_template, url_for, request, session
from bookform import BookmarksForm
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
    # form=BookmarksForm()
    if request.method == 'POST':
        session['option'] =request.form['category']
    else:
        try:          
         if session['option'] == None:
            session['option']='Python'
        except :
            session['option']='Python'
        
    page = request.args.get('page', 1, type=int)
    data = Bookmarks.query.filter_by(catagory=session['option']).paginate(page=page) #Start paginating
    return render_template('book.html', title=session['option'], form=data)

@app.route("/book/", methods=['GET', 'POST'])
# @app.route("/book/<int:id>/update", methods=['GET', 'POST'])
# def bookedit(id):
def bookedit1():
    form=BookmarksForm()
    if form.is_submitted() and  request.method == 'POST':
        # return "%s %s %s" % (request.form.get("catagory"), form.url.data, form.details.data)
        rec=Bookmarks(catagory=request.form.get('catagory'), details=form.details.data, url=form.url.data)
        db.session.add(rec)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('bookedit.html', title='Add bookmarks', form=form)

@app.route("/book/<int:id>/update", methods=['GET', 'POST'])
def bookedit(id):
    form=BookmarksForm()
    rec=Bookmarks.query.get_or_404(id)
    if form.is_submitted():
        # rec.catagory=form.catagory.data
        rec.catagory=request.form.get('catagory')
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
    def __init__(self, catagory, details, url):
        self.catagory = catagory
        self.details = details
        self.url = url
    def __repr__(self):
        return '<Bookmarks %r>' % self.details    

if __name__ == '__main__':
    app.run(debug=True)