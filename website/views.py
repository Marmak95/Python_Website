from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

"""
This is where the front-end views is handled when the user interacts on the website.
"""

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if(request.method == "POST"):
        note = request.form.get("note")

        if(len(note) < 1):
            flash("The note is too short.", category="error")
        else:
            newNote = Note(data=note, userId=current_user.id)
            db.session.add(newNote)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)

# Takes in data as a POST request, load it as a JSON object,
# then access the noteId (from the JS file), then check if it can be deleted
# and lastly delete the note.
@views.route("/delete-note", methods=["POST"])
def deleteNote():
    note = json.loads(request.data) # This function expects a JSON from the index.js file.
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if(note):
        if(note.userId == current_user.id):
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})