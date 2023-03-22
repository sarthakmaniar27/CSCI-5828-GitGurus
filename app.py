from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'AppSecretKey'     

user = {"username": "admin", "password": "password"}

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        if username == user['username'] and password == user['password']:
            
            session['user'] = username
            return redirect('/dashboard')

        return render_template("login.html", error="Invalid credentials") 

    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return '<h1>Upcoming Project for Crime Report</h1>'

    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
