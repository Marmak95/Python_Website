from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

"""
This is where the front-end views is handled when the user interacts on the website.
"""

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", user=current_user)
