from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Advertisement
import os

"""
This is where the front-end views is handled when the user interacts on the website.
"""

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    # Print or use the information as needed
    print("--------------- USER INFO ---------------")
    print(f"User ID: {current_user.id}")
    print(f"Role: {current_user.role}")
    print(f"Email: {current_user.email}")
    print(f"First Name: {current_user.firstName}")
    print(f"Last Name: {current_user.lastName}")
    print("-----------------------------------------")

    if request.method == "POST":
        title = request.form.get("advertisementTitle")
        description = request.form.get("advertisementDescription")
        category = request.form.get("category")

        # Handle file upload
        if("advertisementImage" in request.files):
            file = request.files["advertisementImage"]
            if(file.filename != ""):
                # Save the file to the 'uploads' directory
                filePath = os.path.join("uploads", file.filename)
                file.save(filePath)

                # 'file_path' is stored in the database along with other details like title, description, etc.
                new_advertisement = Advertisement(userId=current_user.id, title=title, description=description, image=filePath, categoryId=category)
                db.session.add(new_advertisement)
                db.session.commit()

                flash("Advertisement added successfully!", category="success")
                return redirect(url_for("views.home"))

    return render_template("home.html", user=current_user)
