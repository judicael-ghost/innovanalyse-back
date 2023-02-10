from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialisation de SQLAcheky
db = SQLAlchemy()

# Initialisation de Flask
app = Flask(__name__)

# Configuration de l'URI
app.config["SQLQALCHEMY_DATABASE_URI"] = "sqlite:///dbase.db"

# Initialisation de l'application
db.init_app(app)

#Creation de Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


# Lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)