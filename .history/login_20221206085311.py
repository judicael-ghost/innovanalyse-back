from flask import Flask, jsonify, request, session
from flask_mysqldb import MySQL, MySQLdb
from werkzeug.security import check_password_hash
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Rayana1234'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_innovanalyse'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



@app.route('/')
def accueil():

    if 'username' in session:
        username = session['username']
        return jsonify({'message': 'You are alredy logged', 'username': username})
    
    else:
        reponse = jsonify({'message':'Unauthorization'})
        reponse.status_code = 401

        return reponse

@app.route('/login', methods=['POST'])
def login():
    _json = request.json
    _username = _json['username']
    _password = _json['password']

    print(_password)

    if _username and _password: 

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = "SELECT * FROM compte WHERE username=%s"
        sql_here = (_username,)

        cursor.execute(sql, sql_here)
        row = cursor.fetchone()

        username = cursor.fetchone['username']
        password = cursor.fetchone['password'] 

        if row:
            if check_password_hash(password, _password):
                session['username'] = username
                cursor.close()
                return jsonify({'message': 'Authenfication réussie'})
            else:
                reponse = jsonify({'message': 'Invalid password'})
                reponse.status_code = 400
                return reponse
    else: 
        reponse = jsonify({'message': 'Invalid credantial'})
        reponse.status_code = 400
        return reponse