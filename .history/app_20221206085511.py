from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialisation de SQLAcheky
db = SQLAlchemy()

# Initialisation de Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)