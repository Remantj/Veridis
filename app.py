from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from python_sql import *

app = Flask(__name__)
autorisation = False

@app.route("/")
def aff_connexion():
    global autorisation
    autorisation = False
    return render_template("connexion.html")

@app.route('/connexion',methods = ['POST'])
def connexion():
    global autorisation
    result = request.form
    identifiant = result["identifiant"]
    mdp = result["mot_de_passe"]
    if identification(identifiant, mdp):
        autorisation = True
        return redirect(url_for("home"))
    return "<h1> Mauvais Identifiant ou Mauvais Mot de Passe </h1>"

@app.route('/aff_inscription')
def aff_inscription():
    return render_template("inscription.html")

@app.route('/inscription', methods = ['POST'])
def inscription():
    result = request.form
    identifiant = result["identifiant"]
    mdp = result["mot_de_passe"]
    inscriptionbd(identifiant, mdp)
    return render_template("connexion.html")

@app.route("/home")
def home():
    return render_template("home.html")
    #return "<h1> Vous n'avez pas accès à cette page </h1>"

@app.route("/home/settings")
def settings():
    return render_template("settings.html")
    #return "<h1> Vous n'avez pas accès à cette page </h1>"

@app.route("/home/stats")
def stats():
    if autorisation:
        return render_template("stats.html", jour=nb_intrusions("jour"), semaine=nb_intrusions("semaine"), mois=nb_intrusions("mois"), annee=nb_intrusions("annee"))
    return "<h1> Vous n'avez pas accès à cette page </h1>"

if __name__ == '__main__':
    app.run(debug="TRUE")
   