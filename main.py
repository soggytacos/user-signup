from flask import Flask, redirect, render_template, request
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def email_validator(email):
    count_at = 0
    count_period = 0
    count_space = 0
    count_email = 0
    for i in email:
        count_email = count_email + 1
        if i == "@":
            count_at = count_at + 1
        else:
            count_at = count_at
        if i == ".":
            count_period = count_period + 1
        else:
            count_period = count_period
        if i == " ":
            count_space = count_space + 1
        else:
            count_space = count_space
    if (count_period != 1) or (count_at != 1) or (count_space > 0) or (count_email > 20 or count_email < 3):
        return False
    else:
        return True

@app.route("/")
def index():
    username_encoded_error = request.args.get("usernameerror")
    password_encoded_error = request.args.get("passworderror")
    vpassword_encoded_error = request.args.get("vpassworderror")
    email_encoded_error = request.args.get("emailerror")
    return render_template('signup.html', usernameerror=username_encoded_error, 
    passworderror=password_encoded_error, vpassworderror=vpassword_encoded_error,
    emailerror=email_encoded_error)

@app.route("/confirmation", methods=['POST'])
def create_user():
# assigns the input values from the form to python variables.
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verify-password']
    email = request.form['email']
# 1.a. checks to ensure that no values are blank.
    if (not username) or (username.strip() == ""):
        usernameerror = "Please add a username.".format(username)
        return redirect("/?usernameerror=" + usernameerror)
    if (not password) or (password.strip() == ""):
        passworderror = "Please add a password.".format(password)
        return redirect("/?passworderror=" + passworderror)
    if (not verifypassword) or (verifypassword.strip() == ""):
        vpassworderror = "Please validate your password.".format(verifypassword)
        return redirect("/?vpassworderror=" + vpassworderror)

#1.b. Validates the username and the strength of the password.
    if (len(username) < 3 or len(username) > 20):
        usernameerror = """Username must be more than 3 characters or 
        less than 20 characters.""".format(username)
        return redirect("/?usernameerror=" + usernameerror)
    if (len(password) < 3 or len(password) > 20):
        passworderror = """Password must be more than 3 characters or
        less than 20 characters""".format(password)
        return redirect("/?passworderror=" + passworderror)

#1.c. Validates the password.
    if not (verifypassword == password):
        vpassworderror = "Passwords do not match.".format(verifypassword)
        return redirect("/?vpassworderror=" + vpassworderror)

#1.d. Validates the email.
    if len(email) > 0:
        if (not email_validator(email)):
            emailerror = "Not a valid email.".format(email)
            return redirect("/?emailerror=" + emailerror)

    return render_template('confirmation.html', username=username)


app.run()
