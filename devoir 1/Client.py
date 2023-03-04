class Client:
    
    #constructeur
    def __init__(self, num = int(), nom = str(), address = str(), cp = str(), ville = str(), nbKm = int()):
        self.__numero = num
        self.__nom = nom
        self.__adresse = address
        self.__codePostale = cp
        self.__ville = ville
        self.__nbKm = nbKm
    
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
    
    #getteur et setteur de adresse
    def _get_adresse(self):
        return self.__adresse
    
    def _set_adresse(self, newAdd = str()):
        self.__adresse = newAdd
    
    adresse = property(_get_adresse, _set_adresse)
    
    #getteur et setteur de codePostale
    def _get_cp(self):
        return self.__codePostale
    
    def _set_cp(self, newCP = str()):
        self.__codePostale = newCP
    
    codePostale = property(_get_cp, _set_cp)
    
    #getteur et setteur de ville
    def _get_ville(self):
        return self.__ville
    
    def _set_ville(self, newVille = str()):
        self.__ville = newVille
    
    ville = property(_get_ville, _set_ville)
    
    #getteur et setteur de nbKm
    def _get_km(self):
        return self.__nbKm
    
    def _set_km(self, newKm = int()):
        self.__nbKm = newKm
    
    nbKm = property(_get_km, _set_km)
    
    #fonction distance()
    def distance(self):
        return self.nbKm

   
    