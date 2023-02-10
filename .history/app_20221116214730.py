from flask import Flask, jsonify, request, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_inovanalyse'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/login')
def login():
    password = generate_password_hash('Rayan123')
    print(password)

    if 'username' in session:
        username = session['username']
        return jsonify({'message': 'You are alredy logged', 'username': username})



if __name__ == '__main__':
    app.run(debug=True, port=3000)