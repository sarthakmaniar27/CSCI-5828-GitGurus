from flask import Flask, render_template, request, redirect, session
import psycopg2
from psycopg2 import sql
import datetime
import re

app = Flask(__name__)
app.secret_key = 'AppSecretKey'     

# Define the database connection parameters
conn = psycopg2.connect(
    dbname="d47mo5ptdsndqo",
    user="uxxmtbozmyqsct",
    password="af63b7f71c902462a550ce8b641650871ce967720c1cc371bb048674c6a38884",
    host="ec2-3-217-146-37.compute-1.amazonaws.com",
    port="5432"
)

# user = {"username": "admin", "password": "password"}

@app.route('/')
def index():
    #return render_template("about.html")
    return redirect('/login')



@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        '''
            Code for Searching in the database and delete the code below
        '''    
        # Create a cursor
        cur = conn.cursor()

        # Use the cursor to execute the SELECT statement
        cur.execute(
            sql.SQL("SELECT * FROM UserData WHERE username = %s AND password = %s"),
            [username, password]
        )

        # Fetch the result of the SELECT statement
        user = cur.fetchone()

        # Close the cursor
        cur.close()

        # If the result is not None, the login was successful
        if user is not None:
            # Set the session variable for the user
            session['username'] = user[1]
            # Redirect to the home page
            return redirect('/dashboard')
        else:
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
        ## check if the passwords are same
        if password != confirm_password:
            return render_template('register.html', error="Passwords do not match")
        
        # Use datetime to create the current date and time
        now = datetime.datetime.now()

        # Format the current date and time as a string in the desired format
        created_on = now.strftime('%Y-%m-%d %H:%M:%S')

        # Create a cursor
        cur = conn.cursor()

        # Use the cursor to execute the INSERT statement
        cur.execute(
            sql.SQL("INSERT INTO UserData (username, password, email, created_on) VALUES (%s, %s, %s, %s)"),
            [username, password, email, created_on]
        )

        # Commit the transaction
        conn.commit()

        # Close the cursor
        cur.close()

        # Set the session variable for the user
        session['username'] = username
        return redirect('/dashboard')
    
    return render_template('register.html')



@app.route('/dashboard')
def dashboard():
    if('username' in session):
        return render_template('dashboard.html')
    return redirect('/login')


@app.route('/logout')
def logout():
    # Remove the session variable for the user
    if 'username' in session:
        session.pop('username', None)
    return redirect('/login')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
