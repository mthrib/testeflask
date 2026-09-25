from app import app
from flask import render_template , url_for, redirect

from app.forms import TesteForms


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = TesteForms()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    return render_template('login.html', form=form)