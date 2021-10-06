from flask import Flask, render_template

app = Flask(__name__)

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

