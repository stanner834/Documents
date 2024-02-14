from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for user accounts (for demonstration purposes)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        users[username] = password
        # Redirect to the homepage with a query parameter indicating successful registration
        return redirect(url_for('index', registered=True))
    else:
        return 'Username and password are required.'

if __name__ == '__main__':
    app.run(debug=True)


