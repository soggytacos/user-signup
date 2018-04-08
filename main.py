from flask import Flask, redirect, render_template, request
import cgi
from functions import email_validator

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')


@app.route("/confirmation", methods=['POST'])
def create_user():
# assigns the input values from the form to python variables.
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verify-password']
    email = request.form['email']
    usernameerror = ""
    passworderror = ""
    vpassworderror = ""
    emailerror = ""
    
# 1.a. checks to ensure that no values are blank.
    if (not username) or (username.strip() == ""):
        usernameerror = "Please add a username."
        username = ""
    if (not password) or (password.strip() == ""):
        passworderror = "Please add a password."
        password = ""
    if (not verifypassword) or (verifypassword.strip() == ""):
        vpassworderror = "Please validate your password."
        verifypassword = ""

#1.b. Validates the username and the strength of the password.
    if (len(username) < 3 or len(username) > 20):
        usernameerror = """Username must be more than 3 characters or 
        less than 20 characters."""
    if (len(password) < 3 or len(password) > 20):
        passworderror = """Password must be more than 3 characters or
        less than 20 characters"""

#1.c. Validates the password.
    if not (verifypassword == password):
        vpassworderror = "Passwords do not match."

#1.d. Validates the email.
    if len(email) > 0:
        if (not email_validator(email)):
            emailerror = "Not a valid email."
 
    if (usernameerror == "") and (passworderror == "") and (vpassworderror == "") and (emailerror == ""):
        return render_template('confirmation.html', username=username)
    else:
        return render_template('signup.html', usernameerror=usernameerror, 
        passworderror=passworderror, vpassworderror=vpassworderror,
        emailerror=emailerror, username=username, password=password, 
        verifypassword=verifypassword, email=email)


app.run()
