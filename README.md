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

![Home_page](https://github.com/Marmak95/Python_Website/assets/79858654/9b4b5435-9881-45ac-8ab9-22aced9964cf)

![Home_page_2](https://github.com/Marmak95/Python_Website/assets/79858654/34c294d9-88e8-4572-ac97-cc87041e1b60)

![admin_page](https://github.com/Marmak95/Python_Website/assets/79858654/de17e11b-5ea7-46f7-89df-9e4b977308b1)

![admin_page_add_category](https://github.com/Marmak95/Python_Website/assets/79858654/9ad1c1b1-5f14-4fbf-a6f7-a43a4dabe8d0)

## Main features added
1. Users can sign up to create an account.
2. Users can login with their created account.
3. Users can logout once they have logged in.
4. Users can become an admin.
5. Users can't access the admin page.
5. Admins can add categories.

## Limitations
1. The users can't add advertisements or see other user's advertisements yet, the functionality will be added.
2. Search functionality is not added yet.
3. Category functionality is not added yet.
4. Admins can only add categories.

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