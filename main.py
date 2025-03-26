from flask import Flask, render_template, request
app = Flask(__name__)

babysitter = {
    "a_doriane" : {
        "pic" : "/images/a_doriane.jpg",
        "nom" : "Dorianne A",
        "age" : 21,
        "genre" : "Femme",
        "qualite" : ["Motivée", "Énergétique", "Bienveillante"],
        "domaine" : ["Maisons"]
    },
    "b_aitana" : {
        "pic" : "/images/b_aitana.jpg",
        "nom" : "Aïtana B",
        "age" : 27,
        "genre" : "Femme",
        "qualite" : ["Sportive", "Motivante", "Coopérative"],
        "domaine" : ["Écoles", "Sorties"]
    },
    "c_marion" : {
        "pic" : "/images/c_marion.jpg",
        "nom" : "Marion C",
        "age" : 23,
        "genre" : "Femme",
        "qualite" : ["Créative", "Curieuse", "Attentive"],
        "domaine" : ["Maisons"]
    },
    "f_thomas" : {
        "pic" : "/images/f_thomas.jpg",
        "nom" : "Thomas F",
        "age" : 25,
        "genre" : "Homme",
        "qualite" : ["Assidû", "Calme", "Prévoyant"],
        "domaine" : ["Écoles", "Sorties", "Anniversaires"]
    },
    "h_thierry" : {
        "pic" : "/images/f_thomas.jpg",
        "nom" : "Thierry H",
        "age" : 47,
        "genre" : "Homme",
        "qualite" : ["Logique", "Réfléchi", "Déterminé"],
        "domaine" : ["Écoles", "Sorties"]
    },
    "ii_elizabeth" : {
        "pic" : "/images/f_thomas.jpg",
        "nom" : "Elizabeth II",
        "age" : 98,
        "genre" : "Femme",
        "qualite" : ["Tolérante", "Sage", "Fiable"],
        "domaine" : ["Maisons", "Écoles","Anniversaires", "Sorties"]
    },
    "m_julie" : {
        "pic" : "/images/m_julie.jpg",
        "nom" : "Julie M",
        "age" : 19,
        "genre" : "Femme",
        "qualite" : ["Ambitieuse", "Enthousiaste", "Ponctuelle"],
        "domaine" : ["Maisons"]
    },
    "p_brad" : {
        "pic" : "/images/p_brad.jpg",
        "nom" : "Brad P",
        "age" : 61,
        "genre" : "Homme",
        "qualite" : ["Honnête", "Modeste", "Généreux"],
        "domaine" : ["Écoles", "Anniversaires"]
    },
    "v_blanche" : {
        "pic" : "/images/v_blanche.jpg",
        "nom" : "Blanche V",
        "age" : 32,
        "genre" : "Homme",
        "qualite" : ["Sociable", "Souriant", "Organisé"],
        "domaine" : ["Maisons"]
    },
    "z_zoe" : {
        "pic" : "/images/z_zoe.jpg",
        "nom" : "Zoé Z",
        "age" : 31,
        "genre" : "Femme",
        "qualite" : ["Adaptable", "Positive", "Innovante"],
        "domaine" : ["Maisons", "Sorties"]
    }
}


@app.route("/")
def hello():
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


app.run(host='0.0.0.0', port=8000)

