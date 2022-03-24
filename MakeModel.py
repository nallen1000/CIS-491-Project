import sqlite3 as sql

global connection
global cursor

connection = sql.connect('aircraftDB')
cursor = connection.cursor()

class Aircraft():
    def __init__(self, acft_make, acft_model):
        self.acft_make = acft_make
        self.acft_model  = acft_model
        
    def getAirList(self):
        return [self.acft_make, self.acft_model]
    
def callDatabase():
    displayMake()
    # displayMakeModel()
    
def displayMake():
    cursor.execute("""SELECT * FROM aircraft WHERE acft_make = ?;""")
    result = cursor.fetchall()
    
    for names in result:
        print("\n    ", names[0])
        
# def displayMakeModel():
    
#     cursor.execute("""SELECT * FROM aircraft WHERE acft_model = ?;""")
#     result = cursor.fetchall()
    
#     for names in result:
#         print("\n    ", names[0])
        
callDatabase()
connection.close()