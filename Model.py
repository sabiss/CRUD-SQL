from Banco import Banco

class Model():
    def __init__(self, tbName):
        self.banco = Banco(tbName)
    
    def read_one_sensor(self, idSensor):
        return self.banco.selectOne(idSensor)