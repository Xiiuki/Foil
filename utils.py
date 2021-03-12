import sqlite3
import requests
import json
import io
import shutil
import os
from datetime import datetime
import schedule
import time


#<---------- Premier script ---------->
""" Script d'interrogation de l'API; récupère les infos de 3 stations; insère les données récupérées dans la BDD 'winds.db'"""

def loop():
    
    station = [410, 432, 113]

    foil = []
    
    try:
    
        for e in station :
    
            requete = f"http://api.pioupiou.fr/v1/live-with-meta/{e}"

            response = requests.get(requete)
        
            response_dict = response.json()
    
            foil.append(response.json())
    
        db = sqlite3.connect('winds.db')

        cursor = db.cursor()

        for data in foil:
    
            data = data['data']
    
            cursor.execute("""INSERT INTO measurement (id,
                                                       latitude,
                                                       longitude,
                                                       state,
                                                       date,
                                                       wind_heading,
                                                       wind_speed_avg,
                                                       wind_speed_max,
                                                       wind_speed_min)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                             (data['id'],
                              data['location']['latitude'],
                              data['location']['longitude'],
                              data['status']['state'],
                              data['measurements']['date'],
                              data['measurements']['wind_heading'],
                              data['measurements']['wind_speed_avg'],
                              data['measurements']['wind_speed_max'],
                              data['measurements']['wind_speed_min'])
                           )

            db.commit()

            print("Insertion effectuée", datetime.now())

    except:
        print("Dommage, essaye encore", datetime.now())
        
    finally:
        cursor.close()
        db.close()
        
        
#<---------- Deuxième script ---------->
""" Vérifie le nombre de lignes dans la BDD 'winds.db'"""        
        
def check_row_number():
    
    with sqlite3.connect("winds.db") as db:
        cursor = db.cursor()
        cursor.execute('''SELECT COUNT(rowid) from measurement ''')
        count = cursor.fetchall()
        return (count[0][0])    
    
#<---------- Troisième script ---------->
""" Permet de supprimer les 3 premières lignes de la BDD 'winds.db'"""    
    
def del_rows():

    with sqlite3.connect("winds.db") as db:
        cursor = db.cursor()
        cursor.execute('''DELETE
                          FROM measurement
                          WHERE rowid IN (Select rowid from measurement limit 3);
                        ''')
                
#<---------- Quatrième script ---------->
""" Compile le script 2 et 3 : si le nombre de lignes est > 9 alors les 3 premières lignes de la BDD 'winds.db' sont
    supprimées et nous pouvons donc insérer 3 nouvelles mesures pour toujours avoir au maximum 12 mesures"""
            
            
def gestion():

    from datetime import datetime
    
    if check_row_number() > 9 :
        del_rows()
        print ("Delete succeed :", check_row_number(), "rows in Database", datetime.now())
    
    else :
        print ("Nothing to delete", datetime.now())
        
#<---------- Cinquième script ---------->
""" Scripts de sauvegarde : 2 méthodes pour sauvegarder la BDD"""        
        
def create_readable_dbcopy():
    
    #create a .sql file as a backup in Backup folder
    
    conn = sqlite3.connect('winds.db')
    with io.open('Backup/winds_dump.sql', 'w') as f:
        for measurement in conn.iterdump():
            f.write('%s\n' % measurement)
            
    print('Backup performed successfully.', datetime.now())
    
    conn.close()
    
    
    
def create_copy_db():

    #create a copy of the database as a backup in Backup folder
     
    try:
        path='C:/Users/joris/Documents/Simplon/Dev_data/Vents/Foil'
    
        shutil.copyfile('winds.db','C:/Users/joris/Documents/Simplon/Dev_data/Vents/Foil/Backup/winds.db')
 
        print("Success copying winds.db", datetime.now())
    
    except:
        print("error while copying winds.db")
        
#<---------- Sixième script ---------->
""" Utilisation du module schedule : gestion du lancement des scripts pour faire tourner l'application foil"""        

def foil():
    
    gestion()
    loop()       
    schedule.every(50).seconds.do(gestion)
    schedule.every(1).minutes.do(loop)
    schedule.every(130).seconds.do(create_copy_db)
    schedule.every(130).seconds.do(create_readable_dbcopy)

    while True:
        schedule.run_pending()
        time.sleep(1)