from flask import Flask, render_template, request, redirect, session
import re

app = Flask(__name__)
app.secret_key = 'AppSecretKey'     

user = {"username": "admin", "password": "password"}

@app.route('/')
def index():
    return redirect('/dashboard')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        '''
            Code for Searching in the database and delete the code below
        '''     
        if username == user['username'] and password == user['password']:
            session['user'] = username
            return redirect('/dashboard')

        return render_template("login.html", error="Invalid credentials") 

    return render_template("login.html")

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')

        # Check for valid email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return render_template("register.html", error="Invalid email address")

        username = request.form.get('username')

        # Check for valid username
        if len(username) < 8 or len(username) > 12:
            return render_template("register.html", error="Length of username should be 8 to 12 characters")
        
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        '''
            code to insert the information into the database
        '''

        ## check if the passwords are same
        if password != confirm_password:
            return render_template('register.html', error="Passwords do not match")
        
        return redirect('/login')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
