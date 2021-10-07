from flask import Flask, render_template, flash,url_for, redirect
from forms import RegistrationForm, LoginForm, Knowledgebase
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1ecc4ba444d91d97d0da200bdde1da7'  #To protect from attacks  python -m secrets  "secrets.token_hex(16)"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'   #use Sqlite location for SQLAlchemy
db = SQLAlchemy(app)  ##Instantiate DB, python > from app import db, db.create_all()

@app.route("/")
def home():
    form = knowledgebase.query.all()
    return render_template("Know.html", title='Get All', form=form)


@app.route("/search")
def pks():
    return render_template("KnowSearch.html")


@app.route("/add", methods=['GET','POST'])
def pka():
    form = Knowledgebase()
    if form.is_submitted():
        rec = knowledgebase(category=form.category.data, subcategory=form.subcategory.data, subject=form.subject.data, description=form.description.data)
        db.session.add(rec)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("KnowAdd.html", title='Add records', form=form)

@app.route("/view/<int:id>/update", methods=['GET', 'POST'])  ## int: to force integer
def pku(id):
    # rec = knowledgebase.query.get_or_404(id=id)
    rec = knowledgebase.query.filter_by(id=id).first_or_404()
    form = Knowledgebase()
    if form.is_submitted():
        # rec = knowledgebase(category=form.category.data, subcategory=form.subcategory.data, subject=form.subject.data, description=form.description.data, id=form.id.data)
        rec.category=form.category.data;rec.subcategory=form.subcategory.data;rec.subject=form.subject.data
        rec.description=form.description.data
        # rec.id=form.id.data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        form.category.data=rec.category
        form.subcategory.data=rec.subcategory
        form.subject.data=rec.subject
        form.description.data=rec.description
        # form.id = rec.id
        return render_template("KnowAdd.html", title=form.subject, form=form, legend='Update')

@app.route("/view/<int:id>", methods=['GET', 'POST'])  ## int: to force integer
def pkv(id):
    form = knowledgebase.query.filter_by(id=id).first_or_404()
    # form = knowledgebase.query.get_or_404(id=id)
    return render_template("KnowView.html", title=form.subject, form=form, legend='Add')

#Use form.py
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    #Verify if the form is submitted successfully
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} ', 'success')
        return redirect(url_for('login')) #to home()

    return render_template("register.html", title="Register User", form=form)  


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login request is submitted', category="success")
        return redirect(url_for('home'))
    return render_template("login.html", title="Login", form=form)



# DB Stuff

class knowledgebase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), unique=False, nullable=False)
    subcategory = db.Column(db.String(30), unique=False, nullable=False)
    subject = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    inserttime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )

def __repr__(self):
        return f"knowledgebase('{self.category}', '{self.subcategory} ', '{self.subject} ', ' {self.inserttime} ' ) "

def how_to_use_db():
    db.session.add(knowledgebase(category='d',subcategory='sb21', subject='s21', description='d2'))
    db.session.add(knowledgebase(category='d',subcategory='sb22', subject='s22', description='d2'))
    db.session.add(knowledgebase(category='d',subcategory='sb23', subject='s23', description='d2'))
    db.session.add(knowledgebase(category='d',subcategory='sb24', subject='s25', description='d2'))
    db.session.add(knowledgebase(category='d',subcategory='sb25', subject='s24', description='d2'))
    db.session.commit()

 
    
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=False, nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('post', backref='author', lazy=True)   ##Foreign key?

    def __repr__(self):
        return f"User('{self.username}', '{self.email} ', '{self.image_file} ' ) "

        "" " This is what you do to create db instance and manually add users " ""
        from app import db
        db.create_all()
        from app import user, post
        user_1 = user(username='chander', email='teste@gmail.com', password='test')
        db.session.add(user_1)
        db.session.add(user_2)
        db.session.commit()

        user.query.all()  #query User table
        user.query.first()  #query User first entry
        user.query.filter_by(username='chander').all()  ## filter  all()  first()
        user.query.get(1)  #get 2, 3, 4th records
        u = user.query.get(1)
        u.id, u.username, u.password  ## get the data from user class
        
        p1 = post(title='Blog 1', content = 'First blog post', user_id = u.id)
        p2 = post(title='Blog 2', content = 'Second blog post', user_id = u.id)
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()

        db.drop_all()  ## Don't do it

class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),  nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted} ', '{self.id} ' ) "



if __name__ == '__main__':
    app.run(debug=True)