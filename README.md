# VERIDIS

Ce projet est un module de sécurité qui utilise un raspberry pi et programmé en python, sql, html, css et javascript.
Celui-ci dispose de deux capteurs, un capteur sonore et un capteur à Ultrasons afin de détecter un quelconque mouvement.
Si une intrusion est détectée, un mail est envoyé au propriétaire du module afin de l'avertir.

## Structure du code
Le dossier dispose de plusieurs fichiers:
- BDVeridis.sql qui permet de créer la base de données associée au projet
- python_sql.py qui permet d'ajouter de nouvelles données à cette base de données, ou encore de les manipuler
- main.py qui permet d'utiliser les capteurs Grove associés au raspberry
- mail.py qui permet d'envoyer un mail
- app.py qui est le fichier principal, celui-ci appelle la plupart des fichiers du projet, il a pour objectif de créer une page web en utilisant flask (les répertoires classiques d'un projet flask ont été respectés)
  
## Les prérequis
Comme pour tout projet, celui-ci demande des prérequis:
- Il faut au préalable avoir créer une base de données et avoir renseigné le nom de celle-ci, l'identifiant et le mot de passe de l'utilisateur dans le fichier python_sql.py
- Il faut avoir installé au préalable de nombreux modules python:
  - grove.gpio
  - grove.adc
  - numpy
  - smtplib
  - datetime
  - mysql.connector
  - flask
  - multiprocessing

### Installation
- Pour l'installation d'une base de données, vous pouvezsuivre ce lien : https://www.malekal.com/installer-mysql-mariadb-sur-debian-10/
- Pour l'installation des modules python il vous suffit de taper dans un terminal sous UNIX : 
  sudo apt-get install python3-module
avec module le nom du module python à installer.
