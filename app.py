import os
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Configuration via .env
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODÈLES (Respect des exigences BDD) ---

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False) # Nom/Prénom
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Equipement(db.Model):
    """Table unique pour Appareils Photos et Téléscopes """
    id = db.Column(db.Integer, primary_key=True)
    type_objet = db.Column(db.String(20), nullable=False) # 'appareil' ou 'telescope'
    # Attributs communs demandés 
    marque = db.Column(db.String(50), nullable=False)
    modele = db.Column(db.String(50), nullable=False)
    date_sortie = db.Column(db.Integer)
    score = db.Column(db.Integer) # 1 à 5
    categorie = db.Column(db.String(50)) # Amateur, Professionnel, etc.
    resume = db.Column(db.Text) # Pour la page détails
    image_file = db.Column(db.String(100), default='default.jpg')

class Photographie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_file = db.Column(db.String(100), nullable=False)

# --- LOGIQUE D'ACCÈS ---

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Connexion requise pour accéder au site.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- ROUTES AUTHENTIFICATION (10 points) ---

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256')
        new_user = User(
            nom=request.form.get('nom'),
            username=request.form.get('username'),
            password=hashed_pw
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Inscription réussie !", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and check_password_hash(user.password, request.form.get('password')):
            session['user_id'] = user.id
            session['user_nom'] = user.nom
            return redirect(url_for('index'))
        flash("Identifiants incorrects", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# --- ROUTES CONTENU ET TEMPLATES SPÉCIFIQUES ---

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/appareils-photos')
@login_required
def appareils_photos():
    # On filtre sur le type et on envoie vers le template dédié
    liste = Equipement.query.filter_by(type_objet='appareil').all()
    return render_template('appareils-photos.html', items=liste)

@app.route('/telescopes')
@login_required
def telescopes():
    # On filtre sur le type et on envoie vers le template dédié
    liste = Equipement.query.filter_by(type_objet='telescope').all()
    return render_template('telescopes.html', items=liste)

@app.route('/photographies')
@login_required
def photographies():
    photos = Photographie.query.all()
    return render_template('photographies.html', photos=photos)

@app.route('/details/<int:id>')
@login_required
def details(id):
    item = Equipement.query.get_or_404(id)
    return render_template('details.html', item=item)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)