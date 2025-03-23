from flask import Flask, render_template
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
        "qualite" : ["Sociable", "Souriante", "Organisée"],
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
    return render_template(
        "home.html", babysitter = babysitter
    )


app.run(host='0.0.0.0', port=8000)

