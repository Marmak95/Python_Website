from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

"""
This is the back-end for the authorization of the user.
"""

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if the user exists in the database (email is unique).
        user = User.query.filter_by(email=email).first()
        if(user):
            if(check_password_hash(user.password, password)):
                # The password is correct and the user is directed to the home page.
                flash("Logged in successfully!", category="success")
                # Log in the user and remember the user after the session expires.
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods=["GET", "POST"])
def signUp():
    if(request.method == "POST"):
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if(user):
            flash("Email already exists.", category="error")
        elif(len(email) < 4):
            flash("Email must be greater than 3 characters.", category="error")
        elif(len(firstName) < 2):
            flash("First name must be greater than 1 character.", category="error")
        elif(password1 != password2):
            flash("The passwords do not match.", category="error")
        elif(len(password1) < 8):
            flash("The password must have at least 8 characters.", category="error")
        else:
            # Add new user to the database if everything is filled in correctly.
            # Hash the password for security reasons (pbkdf2:sha256 is the method instead of sha256 because of Werkzeug version 2.0.0 and later).
            newUser = User(email=email, firstName=firstName, password=generate_password_hash(password1, method="pbkdf2:sha256"))
            db.session.add(newUser)
            # Update the database with the new user.
            db.session.commit()

            # Log in the user and do not remember the user after the session expires.
            login_user(user, remember=False)
            flash("New account created!", category="success")
            # Redirect the user to the home page.
            return redirect(url_for("views.home"))

    return render_template("signUp.html", user=current_user)
