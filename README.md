# Python website
The website is built using the back-end framework called [Flask](https://flask.palletsprojects.com/en/3.0.x/) and the front-end framework [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
The database will be stored in the "instance" folder once main.py starts to run.
The website will continue to develop and its not fully decided yet what the users should be able to do when logged in.

## Main features
1. Users can sign up to create an account.
2. Users can login with their created account.
3. Users can logout once they have logged in.
4. Users can create notes that only the user can see from the home page.
5. Users can delete their own notes.

## How to use
1. Install the modules
2. Run main.py
3. Visit: http://127.0.0.1:5000

### Modules installed

1. 
```
pip install flask
```
2. 
```
pip install flask-login
```
3. 
```
pip install flask-sqlalchemy
```