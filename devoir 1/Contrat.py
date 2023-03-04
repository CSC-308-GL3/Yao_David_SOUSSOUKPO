from datetime import datetime

from Client import Client


class Contrat:
    
    #constructeur
    def __init__(self, num = int(), date = datetime(), client = Client(), mc = float(), interventions = [], nbIntervention = int()):
        self.__numero = num
        self.__date = date
        self.__client = client
        self.__montantContrat = mc
        self.__interventions = interventions
        self.__nbIntervention = nbIntervention
    
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
    
    #getteur et setteur de client
    def _get_client(self):
        return self.__client
    
    def _set_client(self, newClient = Client()):
        self.__client = newClient
    
    client = property(_get_client, _set_client)
    
    #getteur et setteur de montantContrat
    def _get_mc(self):
        return self.__montantContrat
    
    def _set_mc(self, newMC = float()):
        self.__montantContrat = newMC
    
    montantContrat = property(_get_mc, _set_mc)
    
    #getteur et setteur de interventions
    def _get_interventions(self):
        return self.__interventions
    
    def _set_interventions(self, newInterventions = []):
        self.__interventions = newInterventions
    
    interventions = property(_get_interventions, _set_interventions)
    
    #getteur et setteur de nbIntervention
    def _get_nbI(self):
        return self.__nbIntervention
    
    def _set_nbI(self, newNBI = int()):
        self.__nbIntervention = newNBI
    
    nbIntervention = property(_get_nbI, _set_nbI)
    
    #fonction montant()
    def montant(self):
        return self.montantContrat
    
    #fonction ecart()
    def ecart(self):
        pass