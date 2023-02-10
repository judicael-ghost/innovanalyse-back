from flask import Flask, render_template,jsonify, request, url_for, redirect, session
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Configuration flask
app = Flask(__name__)

username = "rayan"
password = "Rayan9568"
database = "db_cir"

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{database}"

# Secret keys
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Instance de SQLAlchemy pour la création de Model
db = SQLAlchemy()
db.init_app(app)

# Instance de Marshmallow pour la création de schema
ma = Marshmallow(app)

# Instance de API pour créer un api restful
api = Api(app)


"""  MODEL """

# Utilisateur
class User(db.Model):
    __tablename__ = "utilisateur"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    # password = db.Column(db.String)

class UserSchemas(ma.Schema):
    class Meta:
        fields = ("id", "username", "email")
        model = User

user_schema = UserSchemas()
user_schemas = UserSchemas(many=True)


# Feuille de temps
class Temps(db.Model):
    __tablename__ = "temps"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, unique=True, nullable=False)
    prenom = db.Column(db.String)
    fonction = db.Column(db.String)
    brut = db.Column(db.String)
    cotisation = db.Column(db.String)
    cadre = db.Column(db.String)
    entre = db.Column(db.String)
    sortie = db.Column(db.String)
    participation = db.Column(db.String)
    

class TempsSchemas(ma.Schema):
    class Meta:
        fields = ("id", "nom", "prenom", "fonction", "brut", "cotisation", "cadre", "entre", "sortie", "participation")
        model = Temps

temps_schema = TempsSchemas()
temps_schemas = TempsSchemas(many=True)

""" CONTROLLEUR """

## Utilisateur

class UserListRessource(Resource):
    def get(self):
        users = User.query.all()
        return user_schemas.dump(users)

    def post(self):
        user = User(
            username = request.json["username"],
            email = request.json["email"]
        )
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)

api.add_resource(UserListRessource, '/utilisateurs')


## Feuille de temps

class TempsListRessource(Resource):
    def get(self):
        temps = Temps.query.all()
        return temps_schemas.dump(temps)
    
    def post(self):
        temp = Temps(
            nom = request.json["nom"],
            prenom = request.json["prenom"],
            fonction = request.json["fonction"],
            brut = request.json["brut"],
            cotisation = request.json["cotisation"],
            cadre = request.json["cadre"],
            entre = request.json["entre"],
            sortie = request.json["sortie"],
            participation = request.json["participation"]
        )

        db.session.add(temp)
        db.session.commit()
        return temps_schema.dump(temp)
api.add_resource(TempsListRessource, '/feuille_temps')

## Login
@app.route('/')
def accueil():
    if "username" in session:
        username = session["username"]
        return jsonify({
            "message" : "Vous êtes authenfie avec succèss",
            "username": username
        })
    else: 
        message = jsonify({
            "message" : "Erreur d'authenfication"
        })

        message.status_code = 401

        return message

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('accueil'))
    return render_template('login.html')


# Creation de base de données
with app.app_context():
    db.create_all()

# Lancement de l'application
if __name__ == "__main__":
    # Excecuter le serveur
    app.run(debug=True)