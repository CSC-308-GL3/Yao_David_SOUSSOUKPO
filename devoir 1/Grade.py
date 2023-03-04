class Grade:
    
    #constructeur
    def __init__(self, code = str(), libelle = str(), taux = float()):
        self.__code = code
        self.__libelle = libelle
        self.__taux = taux
    
    #getteur et setteur de code
    def _get_code(self):
        return self.__code
    
    def _set_code(self, newCode = str()):
        self.__code = newCode
    
    code = property(_get_code, _set_code)
    
    #getteur et setteur de libelle
    def _get_libelle(self):
        return self.__libelle
    
    def _set_libelle(self, newLibelle = str()):
        self.__libelle = newLibelle
    
    libelle = property(_get_libelle, _set_libelle)
    
    #getteur et setteur de taux
    def _get_taux(self):
        return self.__taux
    
    def _set_taux(self, newTaux = float()):
        self.__taux = newTaux
    
    taux = property(_get_taux, _set_taux)
    
    #fonction tauxHoraire()
    def montant(self):
        return self.taux