# Backend InnovAnalyse
Partie backend de l'application de géneration automatique de livrable financière chez InnovAnalyse

## Requirement

1 - clone le repositorie

2 - installer l'environement virtuel (venv) sur votre machine en excecutant la commande suivante
 => py -3 -m venv venv
 
3 - Activer l'environement virtuel
=> venv\Scripts\activate

4 - Installer les extensions inclus dans requirement.txt
=> pip install -r requirement.txt

5 - Créer un base de données postgresql nommée 
=> db_cir

6 - Modifier l'username et le password (ligne 9 et ligne 10) dans app.py par l'username et password de votre serveur de base de données postgres

7 - Excuter le fichier app.py
=> py app.py ou flask run


## Endpoint

### Utilisateur
- /utilisateurs : liste des tous les utilisateurs
- /utilisateurs (post) : nouveau utilisateur
- /utilisateurs/id : afficher le profile d'un seul utilisateur
- /utilisateurs/id (patch) : modifier un utilisateur
- /utilisateurs/id (delete) : supprimer un utilisateur

### Feuille de temps
- /feuille_temps : Liste des tous les feuille de temps
- /feuille_temps (post) : Nouveau billetin de salaire
- /feuille_temps/id (patch) : Modifier un billetin de salaire
- /feuille_temps/id (delete) : Supprimer un billetin de salaire

