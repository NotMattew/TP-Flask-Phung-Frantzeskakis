from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
app = Flask(__name__)
app.secret_key = "vraiment-tres-secret"  # Pour sécuriser la session

# Simule une base de données simple
users_db = {}

reservations_db = []

@app.route('/reserver', methods=['POST'])
def reserver():
    if 'user' not in session:
        flash('Vous devez être connecté pour réserver.', 'error')
        return redirect(url_for('account'))

    # Récupérer les données du formulaire
    date = request.form.get('date')
    heure_debut = request.form.get('heure_debut')
    heure_fin = request.form.get('heure_fin')
    nombre_enfants = request.form.get('nombre_enfants')
    domaine = request.form.get('domaine')

    # Calcul du temps (en heures)
    format_horaire = "%H:%M"
    debut = datetime.strptime(heure_debut, format_horaire)
    fin = datetime.strptime(heure_fin, format_horaire)
    duree = (fin - debut).seconds // 3600  # durée en heures

    if duree <= 0:
        flash('L\'heure de fin doit être après l\'heure de début.', 'error')
        return redirect(url_for('home'))

    # Créer un dictionnaire de réservation
    reservation = {
        'date': date,
        'heure_debut': heure_debut,
        'heure_fin': heure_fin,
        'duree': duree,
        'nombre_enfants': nombre_enfants,
        'domaine': domaine
    }

    # Ajouter la réservation à la session
    if 'reservations' not in session:
        session['reservations'] = []

    session['reservations'].append(reservation)
    session.modified = True  # Assurez-vous que la session est mise à jour

    flash('Réservation enregistrée avec succès !', 'success')
    return redirect(url_for('account'))


@app.route('/annuler_reservation/<int:index>', methods=['GET'])
def annuler_reservation(index):
    if 'reservations' in session and len(session['reservations']) > index:
        session['reservations'].pop(index)  # Supprimer la réservation
        session.modified = True  # Assurez-vous que la session est mise à jour
        flash('Réservation annulée avec succès.', 'success')

    return redirect(url_for('account'))

@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Veuillez remplir tous les champs.', 'error')
            return redirect(url_for('account'))

        if action == 'register':
            if username in users_db:
                flash('Ce nom d\'utilisateur existe déjà.', 'error')
            else:
                users_db[username] = password
                session['user'] = username
                flash('Compte créé avec succès.', 'success')
                return redirect(url_for('account'))

        elif action == 'login':
            if username in users_db and users_db[username] == password:
                session['user'] = username
                flash('Connexion réussie.', 'success')
                return redirect(url_for('account'))
            else:
                flash('Identifiants invalides.', 'error')

    user = session.get('user')
    return render_template('account.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Déconnexion réussie.', 'success')
    return redirect(url_for('account'))
babysitter = {
    "a_doriane" : {
        "iden" : "a_doriane",
        "pic" : "/images/a_doriane.jpg",
        "nom" : "Doriane A",
        "age" : 21,
        "genre" : "Femme",
        "qualite" : ["Motivée", "Énergétique", "Bienveillante"],
        "domaine" : ["Maisons"]
    },
    "b_aitana" : {
        "iden" : "b_aitana",
        "pic" : "/images/b_aitana.jpg",
        "nom" : "Aitana B",
        "age" : 27,
        "genre" : "Femme",
        "qualite" : ["Sportive", "Motivante", "Coopérative"],
        "domaine" : ["Écoles", "Sorties"]
    },
    "c_marion" : {
        "iden" : "c_marion",
        "pic" : "/images/c_marion.jpg",
        "nom" : "Marion C",
        "age" : 23,
        "genre" : "Femme",
        "qualite" : ["Créative", "Curieuse", "Attentive"],
        "domaine" : ["Maisons"]
    },
    "f_thomas" : {
        "iden" : "f_thomas",
        "pic" : "/images/f_thomas.jpg",
        "nom" : "Thomas F",
        "age" : 25,
        "genre" : "Homme",
        "qualite" : ["Assidû", "Calme", "Prévoyant"],
        "domaine" : ["Écoles", "Sorties", "Anniversaires"]
    },
    "h_thierry" : {
        "iden" : "h_thierry",
        "pic" : "/images/h_thierry.jpg",
        "nom" : "Thierry H",
        "age" : 47,
        "genre" : "Homme",
        "qualite" : ["Logique", "Réfléchi", "Déterminé"],
        "domaine" : ["Écoles", "Sorties"]
    },
    "ii_elizabeth" : {
        "iden" : "ii_elizabeth",
        "pic" : "/images/ii_elizabeth.jpg",
        "nom" : "Elizabeth II",
        "age" : 98,
        "genre" : "Femme",
        "qualite" : ["Tolérante", "Sage", "Fiable"],
        "domaine" : ["Maisons", "Écoles","Anniversaires", "Sorties"]
    },
    "m_julie" : {
        "iden" : "m_julie",
        "pic" : "/images/m_julie.jpg",
        "nom" : "Julie M",
        "age" : 19,
        "genre" : "Femme",
        "qualite" : ["Ambitieuse", "Enthousiaste", "Ponctuelle"],
        "domaine" : ["Maisons"]
    },
    "p_brad" : {
        "iden" : "p_brad",
        "pic" : "/images/p_brad.jpg",
        "nom" : "Brad P",
        "age" : 61,
        "genre" : "Homme",
        "qualite" : ["Honnête", "Modeste", "Généreux"],
        "domaine" : ["Écoles", "Anniversaires"]
    },
    "v_blanche" : {
        "iden" : "v_blanche",
        "pic" : "/images/v_blanche.jpg",
        "nom" : "Blanche V",
        "age" : 32,
        "genre" : "Homme",
        "qualite" : ["Sociable", "Souriant", "Organisé"],
        "domaine" : ["Maisons"]
    },
    "z_zoe" : {
        "iden" : "z_zoe",
        "pic" : "/images/z_zoe.jpg",
        "nom" : "Zoé Z",
        "age" : 31,
        "genre" : "Femme",
        "qualite" : ["Adaptable", "Positive", "Innovante"],
        "domaine" : ["Maisons", "Sorties"]
    }
}


@app.route("/")
def home():
    filtres = babysitter.values()
    
    domaine = request.args.get("domaine")
    genre = request.args.get("genre")
    age_order = request.args.get("age")

    if domaine:
        filtres = [b for b in filtres if domaine in b["domaine"]]
    if genre:
        filtres = [b for b in filtres if b["genre"] == genre]
    if age_order == "asc":
        filtres = sorted(filtres, key=lambda x: x["age"])
    elif age_order == "desc":
        filtres = sorted(filtres, key=lambda x: x["age"], reverse=True)

    return render_template("home.html", babysitter=filtres)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/babysitter/<choix>")
def afficher(choix):
    return render_template("babysitter.html", personne=babysitter[choix])

@app.route('/submit_form', methods=['POST'])
def submit_form():
    return request.form

app.run(host='0.0.0.0', port=8000)

