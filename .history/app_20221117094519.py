from flask import Flask, jsonify, request, session
from flask_mysqldb import MySQL, MySQLdb
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbinnovanalyse'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def accueil():
    password = generate_password_hash('Rayan123')
    print(password)

    if 'nom' in session:
        nom = session['nom']
        return jsonify({'message': 'You are alredy logged', 'nom': nom})
    
    else:
        reponse = jsonify({'message':'Unauthorization'})
        reponse.status_code = 401

        return reponse

@app.route('/login')
def login():
    _json = request.json
    _nom = _json['nom']
    _password = _json['password']




if __name__ == '__main__':
    app.run(debug=True, port=3000)