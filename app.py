from flask import Flask, render_template, flash,url_for, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1ecc4ba444d91d97d0da200bdde1da7'  #To protect from attacks  python -m secrets  "secrets.token_hex(16)"

@app.route("/")
def home():
    return render_template("Know.html")


@app.route("/search")
def pks():
    return render_template("KnowSearch.html")


@app.route("/add")
def pka():
    return render_template("KnowAdd.html")


@app.route("/view")
def pkv():
    return render_template("KnowView.html", title="View")

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
