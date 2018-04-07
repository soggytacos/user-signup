from flask import Flask, redirect, render_template, request
import os
import cgi


app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/create-user")
def create_user():
    return render_template('confirmation.html')



app.run()
