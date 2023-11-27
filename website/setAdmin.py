from website import createApp
from website.models import User, db

"""
Run this file to change a user's role to admin.
"""

def setAdmin(email):
    # Create a Flask app and push an application context
    app = createApp()
    app.app_context().push()

    # Extract the user by email.
    adminUser = User.query.filter_by(email=email).first()

    if adminUser:
        # Update the user's role to 'admin' and update the database.
        adminUser.role = 'admin'
        db.session.commit()
        print(f"User {email} is now an admin.")
    else:
        print(f"User {email} not found.")

if(__name__ == "__main__"):
    # Call the setAdmin function with the email of the user you want to make an admin.
    setAdmin("test@hotmail.com")
