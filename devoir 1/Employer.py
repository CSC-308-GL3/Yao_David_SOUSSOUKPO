from datetime import datetime

from Grade import Grade


class Employer:
    
    #constructeur
    def __init__(self, num = int(), nom = str(), qualification = Grade(), date = datetime()):
        self.__numero = num
        self.__nom = nom
        self.__qualification = qualification
        self.__dateEmbauche = date
    
    #getteur et setteur de numero
    def _get_numero(self):
        return self.__numero
    
    def _set_numero(self, newNum = int()):
        self.__numero = newNum
    
    numero = property(_get_numero, _set_numero)
    
    #getteur et setteur de nom
    def _get_nom(self):
        return self.__nom
    
    def _set_nom(self, newNom = str()):
        self.__nom = newNom
    
    nom = property(_get_nom, _set_nom)
    
    #getteur et setteur de qualification
    def _get_qualification(self):
        return self.__qualification
    
    def _set_qualification(self, newQ = Grade()):
        self.__qualification = newQ
    
    qualification = property(_get_qualification, _set_qualification)
    
    #getteur et setteur de dateEmbauche
    def _get_date(self):
        return self.__dateEmbauche
    
    def _set_date(self, newDate = datetime()):
        self.__dateEmbauche = newDate
    
    dateEmbauche = property(_get_date, _set_date)
    
    #fonction coutHoraire()
    def coutHoraire(self):
        pass
    
    #fonction getAncienete()
    def getAncienete(self, annee = int(), mois = int(), jour = int()):
        date = datetime(annee, mois, jour)
        ancienete = datetime.now() - date
        return ancienete.days