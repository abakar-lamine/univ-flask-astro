# univ-flask-astro

# 🌌 AstroSpace - Plateforme Communautaire d'Astronomie

**Projet Universitaire - L3 SPI-TRI (Université Savoie Mont Blanc)**

AstroSpace est une application web développée avec Flask permettant de répertorier et de comparer du matériel d'astronomie (appareils photos et télescopes) et de partager des photographies spatiales. Ce projet a été réalisé dans le cadre d'un travail pratique (TP) mettant en œuvre une architecture MVC, une base de données relationnelle et une interface moderne.

## 🚀 Fonctionnalités
- **Authentification sécurisée** : Inscription et connexion avec hachage des mots de passe.
- **Gestion du matériel** : Affichage dynamique des appareils photos et télescopes par catégories.
- **Détails techniques** : Page dédiée pour chaque équipement incluant un résumé d'expert.
- **Galerie photo** : Espace communautaire pour visualiser les clichés d'astronomie.
- **Interface responsive** : Design moderne utilisant Bootstrap 5, la police Montserrat et des styles CSS personnalisés.

## 🛠️ Technologies utilisées
- **Backend** : Flask (Python 3)
- **Base de données** : MariaDB / MySQL
- **ORM** : Flask-SQLAlchemy
- **Frontend** : Jinja2, Bootstrap 5 (via Bootstrap-Flask), Google Fonts (Montserrat)
- **Sécurité** : Werkzeug (Hachage PBKDF2)

## ⚙️ Installation et Configuration

Suivez ces étapes pour configurer et lancer le projet localement dans votre environnement :

### 1. Démarrer le service de base de données
Avant toute manipulation, assurez-vous que le serveur MariaDB est actif :
```bash
sudo service mariadb start

### 2. Mise en place de l'application

    Clonez ce dépôt sur votre machine locale.

    Installez les dépendances requises via le fichier prévu à cet effet :
    Bash

pip install -r requirements.txt

Configurez l'environnement : Copiez le fichier .env.example et renommez-le en .env.

Renseignez vos accès : Remplissez le fichier .env avec vos identifiants MariaDB locaux :

    SECRET_KEY : Mettez une chaîne de caractères aléatoire (ex: ma_cle_super_secrete).

    DATABASE_URL : Mettez l'URL de votre base de données (ex: mysql+pymysql://root:@127.0.0.1/astro).

Initialisez la base de données : Exécutez le script suivant pour créer les tables et pré-remplir la base avec le matériel (appareils, télescopes, photos) :
Bash

python seed.py

Lancez le serveur :
Bash

    python app.py

    L'application sera alors accessible par défaut sur http://127.0.0.1:5000.

📂 Structure du projet

    app.py : Logique principale du serveur (routes) et définition des modèles SQLAlchemy.

    seed.py : Script d'injection des données de test.

    static/ : Ressources statiques (images dans img/ et styles dans css/style.css).

    templates/ : Ensemble des vues HTML propulsées par Jinja2.

    .env.example : Modèle de configuration pour les variables d'environnement.