from flask import Flask, redirect, render_template, request, url_for

import requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login_page')
def login():
    return render_template('login_page.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__=="__main__":
    app.run()