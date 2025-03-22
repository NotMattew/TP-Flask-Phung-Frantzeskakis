from flask import Flask, render_template
app = Flask(__name__)

babysitter = {
    "a_doriane" : {
        "pic" : "/images/a_doriane.jpg",
        "nom" : "Dorianne A",
        "age" : 21,
        "genre" : "Femme",
        "qualite" : ["Motivée", "Énergétique", "Bienveillante"],
        "domaine" : [""]
    },
    "b_aitana" : {
        "pic" : "/images/b_aitana.jpg",
        "nom" : "Aïtana B",
        "age" : 27,
        "genre" : "Femme",
        "qualite" : ["Sportive", "Motivante", "Coopérative"],
        "domaine" : [""]
    },
    "c_marion" : {
        "pic" : "/images/",
        "nom" : "Marion C",
        "age" : 23,
        "genre" : "Femme",
        "qualite" : [""],
        "domaine" : [""]
    },
    "f_thomas" : {
        "pic" : "/images/",
        "nom" : "Thomas F",
        "age" : 25,
        "genre" : "Homme",
        "qualite" : ["Assidû", "Calme", "Prévoyant"],
        "domaine" : ["Écoles", "Sorties scolaires"]
    },
    "h_thierry" : {
        "pic" : "/images/",
        "nom" : "Thierry H",
        "age" : 47,
        "genre" : "Homme",
        "qualite" : [""],
        "domaine" : [""]
    },
    "ii_elizabeth" : {
        "pic" : "/images/",
        "nom" : "Elizabeth II",
        "age" : 98,
        "genre" : "Femme",
        "qualite" : [""],
        "domaine" : [""]
    },
    "m_julie" : {
        "pic" : "/images/",
        "nom" : "Julie M",
        "age" : 19,
        "genre" : "Femme",
        "qualite" : [""],
        "domaine" : [""]
    },
    "p_brad" : {
        "pic" : "/images/",
        "nom" : "Brad P",
        "age" : 61,
        "genre" : "Homme",
        "qualite" : [""],
        "domaine" : [""]
    },
    "v_blanche" : {
        "pic" : "/images/",
        "nom" : "Blanche V",
        "age" : 32,
        "genre" : "Homme",
        "qualite" : [""],
        "domaine" : [""]
    },
    "z_zoe" : {
        "pic" : "/images/",
        "nom" : "Zoé Z",
        "age" : 31,
        "genre" : "Femme",
        "qualite" : [""],
        "domaine" : [""]
    }
}


@app.route("/")
def hello():
    return render_template(
        "home.html"
    )


app.run(host='0.0.0.0', port=8000)

