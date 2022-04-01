import sqlite3 as sql

global connection
global cursor

connection = sql.connect('aircraftDB')
cursor = connection.cursor()

#make = 'PIPER'
#model = 'PA 28-180'

def callDatabase(make, model):
    displayMakeModel(make, model)

def displayMakeModel(make, model):
    input = (make, model)
    
    cursor.execute("""SELECT eng_type FROM engines,aircraft
                    WHERE acft_model = ? AND acft_make = ?;""", input)
    cursor.execute("""SELECT inj_person_count FROM injury,aircraft
                    WHERE acft_model = ? AND acft_make = ? AND injury_level = 'FATL';""", input)
    cursor.execute("""SELECT ev_state FROM events,aircraft
                    WHERE acft_model = ? AND acft_make = ?;""", input)
    cursor.execute("""SELECT ev_date FROM events,aircraft
                    WHERE acft_model = ? AND acft_make = ?;""", input)
    cursor.execute("""SELECT eng_mfgr FROM engines,aircraft
                    WHERE acft_model = ? AND acft_make = ?;""", input)

    for names in result:
        print("\n", names[0])

connection.close()