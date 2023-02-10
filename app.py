from flask import Flask, render_template,jsonify, request, url_for, redirect, session
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin

# Configuration flask
app = Flask(__name__)



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

username = "postgres"
password = "judih007"
database = "innovanalyse"

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
    name = db.Column(db.String)
    secteur = db.Column(db.String)
    about = db.Column(db.String)
    email = db.Column(db.String)
    contact = db.Column(db.String)
    adresse = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)

class UserSchemas(ma.Schema):
    class Meta:
        fields = ("id", "username","name","secteur","about", "email","contact","adresse", "password", "role")
        model = User

user_schema = UserSchemas()
user_schemas = UserSchemas(many=True)


# Feuille de temps
class Temps(db.Model):
    __tablename__ = "temps"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, unique=True, nullable=False)
    prenom = db.Column(db.String)
    adresse = db.Column(db.String)
    contact = db.Column(db.String)
    diplome = db.Column(db.String)
    etablissement = db.Column(db.String)
    annee = db.Column(db.String)
    fonction = db.Column(db.String)
    brut = db.Column(db.String)
    cadre = db.Column(db.String)
    cotisation = db.Column(db.String)
    cotisationeligible = db.Column(db.String)
    salairecharge = db.Column(db.String)
    cheure = db.Column(db.String)
    cjours = db.Column(db.String)
    entrer = db.Column(db.String)
    sortie = db.Column(db.String)
    ticket = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
    user = db.relationship("User", backref=db.backref("utilisateur", foreign_keys=[user_id]))
    

class TempsSchemas(ma.Schema):
    class Meta:
        fields = ("id", "nom", "prenom","adresse" ,"contact" , "diplome", "etablissement", "annee",  "fonction", "brut", "cadre", "cotisation", "cotisationeligible", "salairecharge", "cheure", "cjours", "entrer", "sortie", "ticket", "user_id")
        model = Temps

temps_schema = TempsSchemas()
temps_schemas = TempsSchemas(many=True)

class Projet(db.Model):
    __tablename__ = 'projet'
    id = db.Column(db.Integer, primary_key=True)
    projetlib = db.Column(db.String, unique=True, nullable=False)
    projetnom = db.Column(db.String, unique=True, nullable=False)

    usere_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
    usere = db.relationship("User", backref=db.backref("utilisateure" , foreign_keys=[usere_id]))

class ProjetSchemas(ma.Schema):
    class Meta:
        fields = ("id", "projetlid","projetnom","usere_id")
        model = Projet

projet_schema = ProjetSchemas()
projet_schemas = ProjetSchemas(many=True)

class Participer(db.Model):
    __tablename__ = 'participer'
    id = db.Column(db.Integer, primary_key=True) 

    projet_id = db.Column(db.Integer, db.ForeignKey('projet.id'))
    projet = db.relationship("Projet", backref=db.backref("projet", uselist=False))

    salarie_id = db.Column(db.Integer, db.ForeignKey('temps.id'))
    salarie = db.relationship("Temps", backref=db.backref("temps", uselist=False))

    jours = db.Column(db.String(80))

class ParticiperSchemas(ma.Schema):
    class Meta:
        fields = ("id", "projet_id","salarie_id","jours")
        model = Participer

participer_schema = ParticiperSchemas()
participer_schemas = ParticiperSchemas(many=True)

""" CONTROLLEUR """

## Utilisateur
class UserListRessource(Resource):
    # Liste utilisateur
    def get(self):
        users = User.query.all()
        return user_schemas.dump(users)

    # Nouveau utilisateur
    def post(self):
        user = User(
            username = request.json["username"],
            name = request.json["name"],
            secteur= request.json["secteur"],
            about = request.json["about"],
            email = request.json["email"],
            contact = request.json["contact"],
            adresse = request.json["adresse"],
            password = request.json["password"],
            role = request.json["role"]
        )
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)

api.add_resource(UserListRessource, '/utilisateurs' )

# Profile d'utilisateur
class UserProfilResource(Resource):
    # Affiche profil
    def get(self, id):
        profil = User.query.get_or_404(id)
        return user_schema.dump(profil)

    # Modifier un utilisateur
    def patch(self, id):
        user = User.query.get_or_404(id)

        if "username" in request.json :
            user.username = request.json["username"]

        if "name" in request.json :
            user.name = request.json["name"]

        if "secteur" in request.json :
            user.secteur = request.json["secteur"]

        if "about" in request.json :
            user.about = request.json["about"]

        if "email" in request.json:
            user.email = request.json["email"]

        if "contact" in request.json :
            user.contact = request.json["contact"]

        if "adresse" in request.json :
            user.adresse = request.json["adresse"]

        if "password" in request.json:
            user.password = request.json["password"]

        if "role" in request.json:
            user.password = request.json["role"]

        db.session.commit()

        return user_schema.dump(user)

    # Supprimer un utilisateur
    def delete(self, id):
        user = User.query.get_or_404(id)

        db.session.delete(user)
        db.session.commit()
        return '', 204

api.add_resource(UserProfilResource, '/utilisateurs/<int:id>')


## Feuille de temps
class TempsListRessource(Resource):
    # Liste feuille de temps
    def get(self):
        temps = Temps.query.all()
        return temps_schemas.dump(temps)
    
    # Nouveau billetin de salaire
    def post(self):
        temp = Temps(
            nom = request.json["nom"],
            prenom = request.json["prenom"],
            adresse = request.json["adresse"],
            contact = request.json["contact"],
            diplome = request.json["diplome"],
            etablissement = request.json["etablissement"],
            annee = request.json["annee"],
            fonction = request.json["fonction"],
            brut = request.json["brut"],
            cadre = request.json["cadre"],
            cotisation = request.json["cotisation"],
            cotisationeligible = request.json["cotisationeligible"],
            salairecharge = request.json["salairecharge"],
            cheure = request.json["cheure"],
            cjours = request.json["cjours"],
            entrer = request.json["entrer"],
            sortie = request.json["sortie"],
            ticket = request.json["ticket"],
            user_id = request.json["user_id"]
        )

        db.session.add(temp)
        db.session.commit()
        return temps_schema.dump(temp)
api.add_resource(TempsListRessource, '/feuille_temps')


# Editer une billetin de salaire
class EditTempsRessource(Resource):
    # Affiche un billetin de salaire
    def get(self, id):
        billetin = Temps.query.get_or_404(id)
        return temps_schema.dump(billetin)

    # Modifier un billetin de salaire
    def patch(self, id):
        billetin = Temps.query.get_or_404(id)

        if "nom" in request.json:
            billetin.nom = request.json["nom"]

        if "prenom" in request.json:
            billetin.prenom = request.json["prenom"]

        if "adresse" in request.json:
            billetin.adresse = request.json["adresse"]

        if "contact" in request.json:
            billetin.contact = request.json["contact"]

        if "diplome" in request.json:
            billetin.diplome = request.json["diplome"]
        
        if "etablissement" in request.json:
            billetin.etablissement = request.json["etablissement"]

        if "annee" in request.json:
            billetin.annee = request.json["annee"]

        if "fonction" in request.json:
            billetin.fonction = request.json["fonction"]
        
        if "brut" in request.json:
            billetin.brut = request.json["brut"]

        if "cadre" in request.json:
            billetin.cadre = request.json["cadre"]

        if "cotisation" in request.json:
            billetin.cotisation = request.json["cotisation"]

        if "cotisationeligible" in request.json:
            billetin.cotisationeligible = request.json["cotisationeligible"]

        if "salairecharge" in request.json:
            billetin.salairecharge = request.json["salairecharge"]

        if "cheure" in request.json:
            billetin.cheure = request.json["cheure"]

        if "cjours" in request.json:
            billetin.cjours = request.json["cjours"]
        
        if "entrer" in request.json:
            billetin.entrer = request.json["entrer"]
        
        if "sortie" in request.json:
            billetin.sortie = request.json["sortie"]

        if "ticket" in request.json:
            billetin.ticket = request.json["ticket"]

        if "user_id" in request.json:
            billetin.user_id = request.json["user_id"]

        db.session.commit()
        return temps_schema.dump(billetin)


    # Suppprimer un billetin de salaire
    def delete(self, id):
        billetin = Temps.query.get_or_404(id)

        db.session.delete(billetin)
        db.session.commit()

        return '', 204

api.add_resource(EditTempsRessource, '/feuille_temps/<int:id>')


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