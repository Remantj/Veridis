"""
    Ceci est le fichier principal du projet
    il permet de lier tous les autres fichiers
    au sein d'un site web
"""

from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from python_sql import *
import main
import multiprocessing as process
from time import sleep

app = Flask(__name__)
autorisation = False
identifiant = ""
img_active = "veridis_grey.png"
thread = None

@app.route("/")
def aff_connexion():
    """
    Fonction permettant d'afficher la page de connexion au site web
    """
    global autorisation
    autorisation = False
    return render_template("connexion.html")

@app.route('/connexion',methods = ['POST'])
def connexion():
    """
    Fonction permettant la connexion au site web
    """
    global autorisation, identifiant
    result = request.form
    identifiant = result["identifiant"]
    mdp = result["mot_de_passe"]
    if identification(identifiant, mdp):
        autorisation = True
        return redirect(url_for("home"))
    return "<h1> Mauvais Identifiant ou Mauvais Mot de Passe </h1>"

@app.route('/aff_inscription')
def aff_inscription():
    """
    Fonction permettant d'afficher la page d'inscription
    """
    return render_template("inscription.html")

@app.route('/inscription', methods = ['POST'])
def inscription():
    """
    Fonction permettant l'incription au site web
    """
    result = request.form
    identifiant = result["identifiant"]
    mdp = result["mot_de_passe"]
    inscriptionbd(identifiant, mdp)
    return render_template("connexion.html")

@app.route("/home")
def home():
    """
    Fonction permettant d'afficher la page principale
    """
    global identifiant, img_active, autorisation
    if autorisation:
        return render_template("home.html", nom=identifiant, image=img_active)
    return "<h1> Vous n'avez pas accès à cette page </h1>"

@app.route("/home/settings")
def settings():
    """
    Fonction permettant d'afficher la page des paramètres
    """
    global identifiant, autorisation
    if autorisation:
        return render_template("settings.html", nom=identifiant)
    return "<h1> Vous n'avez pas accès à cette page </h1>"

@app.route("/home/stats")
def stats():
    """
    Fonction permettant d'afficher la page des statistiques
    """
    global identifiant, autorisation
    if autorisation:
        return render_template("stats.html", jour=nb_intrusions("jour"), semaine=nb_intrusions("semaine"), mois=nb_intrusions("mois"), annee=nb_intrusions("annee"), nom=identifiant)
    return "<h1> Vous n'avez pas accès à cette page </h1>"

@app.route("/home/capteur", methods= ["POST"])
def capteur():
    """
    Fonction permettant de lancer les capteurs via le fichier main.py,
    capteurs qui sont lancés dans un thread en parallèle de la page web
    """
    global identifiant, img_active, thread
    result = request.form
    if thread != None:
        return "<h1> Veuillez arreter les capteurs au prealable <h1>"
    if "ultrasonic_ranger" in result:
        main.grove_ranger_active = True
    else:
        main.grove_ranger_active = False
    if "sound_sensor" in result:
        main.sound_sensor_active = True 
    else:
        main.sound_sensor_active = False
    if main.grove_ranger_active or main.sound_sensor_active:
        thread = process.Process(target=main.captation)
        thread.start()
        img_active = "veridis_green.png"
    return render_template("home.html", nom=identifiant, image=img_active)

@app.route('/home/bouton', methods=["POST"])
def bouton():
    """
    Fonction permettant de lancer la prise de valeurs de références via le fichier main.py
    """
    global identifiant, img_active
    main.prise_references()
    return render_template("settings.html", nom=identifiant, image=img_active)

@app.route('/home/desactivation', methods=["POST"])
def desactivation():
    """
    Fonction permettant de stopper le thread actif, et donc d'arrêter les capteurs
    """
    global img_active, thread
    if thread != None:
        thread.terminate()
        thread = None
        img_active = "veridis_grey.png"
        return render_template("home.html", nom=identifiant, image=img_active)
    return "<h1> Veuillez demarrer les capteurs au prealable <h1>"

if __name__ == '__main__':
    app.run()
