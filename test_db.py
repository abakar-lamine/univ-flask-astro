from app import app, db, Equipement, Photographie

def peupler_base():
    with app.app_context():
        # On vide les tables pour éviter les doublons
        db.session.query(Equipement).delete()
        db.session.query(Photographie).delete()

        # --- APPAREILS PHOTOS ---
        appareils = [
            Equipement(type_objet='appareil', categorie='Amateur', marque='Canon', modele='EOS 2000D', date_sortie=2018, score=4, resume='Un excellent rapport qualité/prix pour faire ses premiers pas en astrophotographie.', image_file='canon.jpg'),
            Equipement(type_objet='appareil', categorie='Amateur sérieux', marque='Nikon', modele='D7500', date_sortie=2017, score=5, resume='Capteur performant pour capter un maximum de lumière dans le ciel nocturne.', image_file='nikon.jpg'),
            Equipement(type_objet='appareil', categorie='Professionnel', marque='Sony', modele='Alpha 7S III', date_sortie=2020, score=5, resume='Le roi incontesté de la basse lumière. Idéal pour la Voie Lactée.', image_file='sony.jpg')
        ]

        # --- TÉLÉSCOPES ---
        telescopes = [
            Equipement(type_objet='telescope', categorie='Téléscopes pour enfants', marque='Celestron', modele='FirstScope', date_sortie=2015, score=3, resume='Compact et facile à utiliser pour observer les cratères de la Lune.', image_file='celestron.jpg'),
            Equipement(type_objet='telescope', categorie='Automatisés', marque='Sky-Watcher', modele='Mak127 AZ-GTi', date_sortie=2019, score=4, resume='Monture motorisée qui suit les astres automatiquement via smartphone.', image_file='skywatcher.jpg'),
            Equipement(type_objet='telescope', categorie='Téléscopes complets', marque='Orion', modele='SkyQuest XT8', date_sortie=2012, score=5, resume='Le Dobson classique. Diamètre généreux pour explorer le ciel profond.', image_file='orion_telescope.jpg')
        ]

        # --- PHOTOGRAPHIES ---
        photos = [
            Photographie(titre='La Nébuleuse d\'Orion', description='M42 capturée en plein hiver depuis les Alpes.', image_file='nebuleuse.jpg'),
            Photographie(titre='Galaxie d\'Andromède', description='Notre voisine galactique (M31) située à 2,5 millions d\'années-lumière.', image_file='andromede.jpg'),
            Photographie(titre='Éclipse Lunaire', description='Phase totale de l\'éclipse avec sa teinte cuivrée caractéristique.', image_file='eclipse.jpg')
        ]

        # Ajout à la base de données
        db.session.add_all(appareils + telescopes + photos)
        db.session.commit()
        print("✅ Base de données remplie avec succès avec les noms d'images !")

if __name__ == '__main__':
    peupler_base()