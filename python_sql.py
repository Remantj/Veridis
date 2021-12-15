import mysql.connector
from datetime import datetime

#connexion au base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "user",
  password = "root",
  database = "VERIDIS"
)
#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()
#requéte SQL

def ultrasonic_ranger(presence, distance):
  sql = "INSERT INTO RANGER(PRESENCE, DISTANCE, TEMPS) VALUES (%s, %s, %s)"
  #les valeurs de la requéte SQL
  value = (presence, distance, str(datetime.now()))
  #exécuter le curseur avec la méthode execute() et transmis la requéte SQL
  cur.execute(sql, value)
  #valider la transaction
  db.commit()

def sound_sensor(son):
  sql = "INSERT INTO SOUND(SON, TEMPS) VALUES (%s, %s)"
  value = (son, str(datetime.now()))
  cur.execute(sql, value)
  db.commit()

def reference(distance, son):
  sql = "INSERT INTO REFERENCE(DISTANCE, SON, TEMPS) VALUES (%s, %s, %s)"
  value = (distance, son, str(datetime.now()))
  cur.execute(sql, value)
  db.commit()

  