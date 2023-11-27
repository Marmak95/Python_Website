# Python website
The website is built using the back-end framework called [Flask](https://flask.palletsprojects.com/en/3.0.x/) and the front-end framework [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
The database will be stored in a folder called "instance" once main.py starts to run.
The website will continue to develop and it will be similar to the swedish website called "Blocket",
where users can create advertisements for items that they want to sell or if they want to buy
something from another user.
The functionality of the website is prioritized, so the front-end will be focused on when the functionality is added.

## Images
![Login_page](https://github.com/Marmak95/Python_Website/assets/79858654/1712bdf0-6316-4096-879d-286f2d12c95f)

![Sign_up_page](https://github.com/Marmak95/Python_Website/assets/79858654/aef6936a-dd0e-457c-be66-646efeca35ec)

![Home_page](https://github.com/Marmak95/Python_Website/assets/79858654/e8ea7513-6cac-4998-9af3-26ecad60ab9a)

![Home_page_2](https://github.com/Marmak95/Python_Website/assets/79858654/de1be1ef-716d-4710-8b03-0a29b74acc66)

## Main features added
1. Users can sign up to create an account.
2. Users can login with their created account.
3. Users can logout once they have logged in.
4. Users can become an admin.

## Limitations
1. The users can't add advertisements or see other user's advertisements yet, the functionality will be added.
2. Search functionality is not added yet.
3. Category functionality is not added yet.
4. Admins can't do anything special yet.

## How to use
1. Install the modules
2. Change the password in website/secretAppKey.cfg
3. Run main.py to start the server
4. Visit: http://127.0.0.1:5000

### Set admin
1. Sign up an account that will become an admin
2. Cancel the server (ctrl + c in the terminal)
3. Change the email for the user that should become an admin in setAdmin.py at the bottom row.
4. Run setAdmin.py (from ../Python_Website)
```
python -m website.setAdmin
```
5. Start the server again and continue

### Modules installed

```
pip install flask
```
```
pip install flask-login
```
```
pip install flask-sqlalchemy
```