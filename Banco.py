import psycopg2

class Banco():
    
    def __init__(self, tbName):
        self.conn = psycopg2.connect(database='pabd', 
                        host='localhost', 
                        user='postgres', 
                        password='ifrn123', 
                        port='5432')
        self.cursor = self.conn.cursor()
        self.tbName = tbName
        
    def selectOne(self, idSensor):
        self.cursor.execute("SELECT * FROM {} WHERE idsensor = {};".format(self.tbName, idSensor))
        return self.cursor.fetchone()