from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loginonde")
def login():
    return render_template("login.html")

app.run()