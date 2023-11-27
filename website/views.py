from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from . import db
from .models import Advertisement, Category
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

    if(request.method == "POST"):
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

@views.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if(request.method == "POST"):
        action = request.json.get("action")

        if(action == "add_category"):
            category_name = request.json.get("categoryName")

            # Check if the category name already exists in the database.
            existing_category = Category.query.filter_by(name=category_name).first()
            if(existing_category):
                flash("Category already exists!", category="error")
                print(existing_category.name, "already exists!")
                return jsonify({"success": False, "error": "Category already exists"})
            
            # Add category to the database.
            category = Category(name=category_name)
            db.session.add(category)

            try:
                db.session.commit()
                flash("Category added successfully!", category="success")
                print(category.name, "was added!")
                return jsonify({"success": True})
            except IntegrityError as e:
                db.session.rollback()
                print(category.name, "was not added!")
                flash("Category could not be added!", category="error")
                print("IntegrityError:", e)
                return jsonify({"success": False, "error": "Category could not be added"})

        else:
            return jsonify({"success": False, "error": "Invalid action"})

    return render_template("admin.html", user=current_user)


