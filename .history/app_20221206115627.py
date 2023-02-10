from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialisation de SQLAcheky
db = SQLAlchemy()

# Initialisation de Flask
app = Flask(__name__)

# Configuration de l'URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dbase.db"

# Initialisation de l'application
db.init_app(app)

#Creation de Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

#Initialiser la base de donnée
with app.app_context():
    db.create_all()



#Liste des utilisateurs
@app.route('/utilisateur')
def liste():
    users = db.session.execute(db.select(User)).scalars()
    return render_template('user.html', users=users)

# Nouveau utilisateur
@app.route('/utilisateur/nouveau', methods=['GET','POST'])
def nouveau():
    if request.method =='POST':
        user = User(
            username = request.form["username"],
            password = request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        

    return render_template('profil.html')
# Lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)