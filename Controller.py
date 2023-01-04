from tkinter import *

class Controller():
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setCommandSearch(self.buscarSensor)
        self.view.setCommandInsert(self.insertSensor)
        self.view.setCommandDelete(self.deleteSensor)
        self.view.setCommandAlterar(self.atualizarBanco)
        self.view.setCommandCommit(self.commitBanco)
        
    def buscarSensor(self):
        idSensor = self.view.txtidSensor.get()
        sensor  = self.model.read_one_sensor(idSensor)
        self.view.updateBySearch(sensor)
    
    def insertSensor(self):
        idSensor = self.view.txtidSensor.get()
        variavel = self.view.txtVariavel.get()
        medicao = self.view.txtMedicao.get()
        unidade = self.view.txtUnidade.get()
        registro = self.view.txtRegistro.get()
        latitude = self.view.txtLatitude.get()
        longitude = self.view.txtLongitude.get()
        
        self.model.insert_one_sensor(idSensor, variavel, medicao, unidade, registro, latitude, longitude)
        self.view.logUpdate(idSensor)
    
    def deleteSensor(self):
        idSensor = self.view.txtidSensor.get()
        self.model.delete_one_sensor(idSensor)
        self.view.logDelete(idSensor)
        
    def atualizarBanco(self):
        idSensor = self.view.txtidSensor.get()
        variavel = self.view.txtVariavel.get()
        medicao = self.view.txtMedicao.get()
        unidade = self.view.txtUnidade.get()
        registro = self.view.txtRegistro.get()
        latitude = self.view.txtLatitude.get()
        longitude = self.view.txtLongitude.get()

        self.model.updateBanco(variavel, medicao, unidade, registro, latitude, longitude, idSensor)
        self.view.logAtualizar(idSensor)
        
    def commitBanco(self):
        self.model.commit_changes()