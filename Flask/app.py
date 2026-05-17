# Flask runs on server 
# It is use for Web development 
# It is mostly use for integreting our ml models 
# render_template html file ko load krke customer ko dikhata hai 

from flask import Flask, render_template, request
from db import create_table, register_user, search

create_table()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    result = register_user(name, email, password)

    if result: # if user not exists 
        return render_template('login.html', message='Registration successfull. Kindly login to proceed')
    else: # if user exists
        return render_template('register.html', message='Email already exists')
    
@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    result = search(email, password)
    if result==1:
        return 'Login successful'
    else:
        return 'Invalid email or password'
        # return render_template('login.html', message='Invalid email or password')


app.run(debug=True)