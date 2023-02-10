from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# Initialisation de SQLAcheky
db = SQLAlchemy()

# Initialisation de Flask
app = Flask(__name__)

# Configuration base de données
username = "rayan"
password = "Rayan9568"
database = "db_cir"

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{database}"

# Initialisation de l'application
db.init_app(app)
with app.app_context():
    db.create_all()

#Creation de Model
class User(db.Model):
    __tablename__ = "utilisateurs"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)





#Liste des utilisateurs
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



# Lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)