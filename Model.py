from Banco import Banco

class Model():
    def __init__(self, tbName):
        self.banco = Banco(tbName)
    
    def read_one_sensor(self, idSensor):
        return self.banco.selectOne(idSensor)
    
    def delete_one_sensor(self, idSensor):
        self.banco.deleteOne(idSensor)
    
    def insert_one_sensor(self, idSensor, variavel, medicao, unidade, registro, latitude, longitude):
        return self.banco.insertOne(idSensor, variavel, medicao, unidade, registro, latitude, longitude);
    
    def update_one_sensor(self, idSensor, variavel, medicao, unidade, registro, latitude, longitude):
        self.banco.updateOne(idSensor, variavel, medicao, unidade, registro, latitude, longitude);
    
    def updateBanco(self, variavel, medicao, unidade, registro, latitude, longitude, idSensor):
        self.banco.updateBanco(variavel, medicao, unidade, registro, latitude, longitude, idSensor)

    def commit_changes(self):
        self.banco.commitChanges()