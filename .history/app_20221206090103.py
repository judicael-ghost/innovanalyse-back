from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialisation de SQLAcheky
db = SQLAlchemy()

# Initialisation de Flask
app = Flask(__name__)

# Configuration de l'URI
app.config["SQLQALCHEMY_DATABASE_URI"] = "sqlite:///dbase.db"

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)