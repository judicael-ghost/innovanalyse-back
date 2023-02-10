from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialise SQLAcheky
db = SQLAlchemy()

if __name__ == "__main__":
    app.run(debug=True)