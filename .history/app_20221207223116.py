from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy


# Configuration flask
app = Flask(__name__)

username = "rayan"
password = "Rayan9568"
database = "db_cir"

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{database}"

# Secret keys
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Instatiation base de données
db = SQLAlchemy()
db.init_app(app)


"""  MODEL """


# Utilisateur
class User(db.Model):
    __tablename__ = "utilisateur"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)


# Feuille de temps
class Temps():
    __tablename__ = "temps"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String)
    fonction = db.Column(db.String)
    brut = db.Column(db.String)
    cotisation = db.Column(db.String)
    cadre = db.Column(db.String)
    entre = db.Column(db.String)
    sortie = db.Column(db.String)
    participation = db.Column(db.String)
    


""" CONTROLLEUR """

## Utilisateur

# Liste utilisateur
@app.route('/utilisateur')
def liste():
    users = db.session.execute(db.select(User)).scalars()
    return render_template('user.html', users=users)

# Nouveau utilisateur
@app.route("/utilisateur/nouveau", methods=["GET","POST"])
def nouveau():
    if request.method == "POST":
        user = User(
            username = request.form["username"],
            email = request.form["email"]
        )
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("profil", id=user.id))

    return render_template('nouveau.html')

# Profil d'utilisateur
@app.route('/utilisateur/profil/<int:id>')
def profil(id):
    user = db.get_or_404(User, id)
    return render_template("profil.html", user = user)

# Suppression utilisateur
@app.route('/utilisateur/supprimer')
def supprimer():
    return redirect(url_for("liste"))


## Login
@app.route('/')
def accueil():
    if "username" in session:
        return f'Vous etez authentifie en tant que {session["username"]}'
@app.route('/login')
def login():
    session['username'] = request.form['username']


## FEUILLE DE TEMPS
# Liste billetin de salaire
@app.route('/temps')
def feuille_temps():

    pass



# Lancement de l'application
if __name__ == "__main__":
    # Creation de base de données
    with app.app_context():
        db.create_all()
    
    # Excecuter le serveur
    app.run(debug=True)