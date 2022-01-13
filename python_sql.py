"""
  Fichier permettant le lien entre le site web et la base de données
"""

import mysql.connector
from datetime import datetime

#connexion à la base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "user",
  password = "root",
  database = "VERIDIS"
)
#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()

#requêtes SQL
def ultrasonic_ranger(presence, distance):
  """
  Fonction permettant d'insérer des valeurs dans la table RANGER, 
  c'est-à-dire la table gérant les données liées au capteur à ultrasons (Ultrasonic Ranger)
  """
  sql = "INSERT INTO RANGER(PRESENCE, DISTANCE, TEMPS) VALUES (%s, %s, %s)"
  #les valeurs de la requéte SQL
  value = (presence, distance, str(datetime.now()))
  #exécuter le curseur avec la méthode execute() et transmis la requéte SQL
  cur.execute(sql, value)
  #valider la transaction
  db.commit()

def sound_sensor(son):
  """
  Fonction permettant d'insérer des valeurs dans la table SOUND, 
  c'est-à-dire la table gérant les données liées au capteur de son (Sound Sensor)
  """
  sql = "INSERT INTO SOUND(SON, TEMPS) VALUES (%s, %s)"
  value = (son, str(datetime.now()))
  cur.execute(sql, value)
  db.commit()

def reference(distance, son):
  """
  Fonction permettant d'insérer des valeurs dans la table REFERENCE, 
  c'est-à-dire la table gérant les données de références
  """
  sql = "INSERT INTO REFERENCE(DISTANCE, SON, TEMPS) VALUES (%s, %s, %s)"
  value = (distance, son, str(datetime.now()))
  cur.execute(sql, value)
  db.commit()

def identification(identifiant, password):
  """
  Fonction permettant de savoir si l'utilisateur disposant du couple
  (identifiant, password) existe dans la base de données,
  fonction utile afin de valider la connexion ou non au site web
  """
  cur.execute("SELECT IDENTIFIANT, MOTDEPASSE FROM PERSONNE")
  res = cur.fetchall()
  return (identifiant, password) in res

def inscriptionbd(identifiant, password):
  """
  Fonction permettant d'insérer des données dans la table PERSONNE,
  cette fonction permet l'inscription d'un nouvel utilisateur au site web
  """
  sql = "INSERT INTO PERSONNE(IDENTIFIANT, MOTDEPASSE) VALUES (%s, %s)"
  value = (identifiant, password)
  cur.execute(sql, value)
  db.commit()

def nb_intrusions(moment):
  """
  Fonction permettant de connaître le nombre d'intrusions selon le jour actuel,
  la semainne actuelle, le mois actuel et l'année actuelle
  """
  if moment == 'jour':
    cur.execute("SELECT COUNT(PRESENCE) FROM RANGER WHERE DAY(TEMPS)=DAY(NOW())")
  elif moment == "semaine":
    cur.execute("SELECT COUNT(PRESENCE) FROM RANGER WHERE WEEK(TEMPS)=WEEK(NOW())")
  elif moment == "mois":
    cur.execute("SELECT COUNT(PRESENCE) FROM RANGER WHERE MONTH(TEMPS)=MONTH(NOW())")
  elif moment == "annee":
    cur.execute("SELECT COUNT(PRESENCE) FROM RANGER WHERE YEAR(TEMPS)=YEAR(NOW())")
  res = cur.fetchone()
  for i in res:
    return i

def sound_ref():
  """
  Fonction permettant de récupérer le son de référence, c'est-à-dire 
  le son du dernier enregistrement de la table REFERENCE
  """
  cur.execute("select SON from REFERENCE where NUM=(select MAX(NUM) from REFERENCE);")
  res = cur.fetchone()
  if res:  
    for i in res:
      return i

def range_ref():
  """
  Fonction permettant de récupérer la distance de référence, c'est-à-dire 
  la distance du dernier enregistrement de la table REFERENCE
  """
  cur.execute("select DISTANCE from REFERENCE where NUM=(select MAX(NUM) from REFERENCE);")
  res = cur.fetchone()
  if res:
    for i in res:
      return i
