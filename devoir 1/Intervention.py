from datetime import datetime

from Employer import Employer


class Intervention:
    
    #constructeur
    def __init__(self, num = int(), date = datetime(), duree = int(), tarif = float(), technicien = Employer()):
        self.__numero = num
        self.__date = date
        self.__duree = duree
        self.__tarifkm = tarif
        self.__technicien = technicien
    
    #getteur et setteur de numero
    def _get_numero(self):
        return self.__numero
    
    def _set_numero(self, newNum = int()):
        self.__numero = newNum
    
    numero = property(_get_numero, _set_numero)
    
    #getteur et setteur de date
    def _get_date(self):
        return self.__date
    
    def _set_date(self, newDate = datetime()):
        self.__date = newDate
    
    date = property(_get_date, _set_date)
    
    #getteur et setteur de duree
    def _get_duree(self):
        return self.__duree
    
    def _set_duree(self, newDuree = int()):
        self.__duree = newDuree
    
    duree = property(_get_duree, _set_duree)
    
    #getteur et setteur de tarifkm
    def _get_tarif(self):
        return self.__tarifkm
    
    def _set_tarif(self, newT = float()):
        self.__tarifkm = newT
    
    tarifkm = property(_get_tarif, _set_tarif)
    
    #getteur et setteur de technicien
    def _get_technicien(self):
        return self.__technicien
    
    def _set_technicien(self, newTech = Employer()):
        self.__technicien = newTech
    
    technicien = property(_get_technicien, _set_technicien)
    
    #procedure affiche()
    def affiche(self):
        print(f"Intervention:\n\
                \t- Numero: {self.numero}\n\
                \t- Date: {self.date}\n\
                \t- Duree: {self.duree}\n\
                \t- TarifKm: {self.tarifkm}\n\
                \t- Technicien:\n\
                \t\t-- Numero: {self.technicien.numero}\n\
                \t\t-- Nom: {self.technicien.nom}\n\
                \t\t-- Qualification: {self.technicien.qualification}\n\
                \t\t-- Date d'embauche: {self.technicien.dateEmbauche}")
    
    #fonction fraisKm()
    def fraisKm(self, dist = float()):
        return self.tarifkm * dist
    
    #fonction fraisMo()
    def fraisMo(self):
        pass