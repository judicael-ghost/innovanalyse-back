from flask import Flask, jsonify, request, session
from flask_mysqldb import MySQL, MySQLdb
from werkzeug.security import check_password_hash
from flask_cors import CORS
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy



if __name__ == "__main__":
    app.run(debug=True)