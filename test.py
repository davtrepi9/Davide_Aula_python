class Veicolo:
    
    #Incapsulamento:
    # con "__" rendo privati gli attributi e metodi in modo da non poter essere accessi da classi esterne se non tramite metodi appositi

    def __init__(self,marca,modello,anno,accensione):
        self.__marca=marca
        self.__modello=modello
        self.__anno=anno
        self.__accensione=accensione

    def accendi(self):
        self.__accensione=True
    
    def spegni(self):
        self.__accensione=False
    
    def stampa(self):
        return f"Marca: {self.__marca} Modello: {self.__modello} Anno: {self.__anno} Accensione: {self.__accensione}"

    def __get__marca(self):
        return self.__marca
    
    def __get_modello(self):
        return self.__modello
    
    def __get_anno(self):
        return self.__anno
    
    def __set_modello(self,nuovo):
        self.__modello=nuovo

    def __set__marca(self,nuovo):
        self.__marca=nuovo

    def __set_anno(self,nuovo):
        self.__anno=nuovo
    
    def suona_clacson(self):
        return "Clacson funzionante"
    
class Auto(Veicolo):    #Ereditarietà: classe Auto,Furgone,Motocicletta sono classi figlie di Veicolo #super() mi richiama init della classe padre

    def __init__(self, marca, modello, anno, accensione,numero_porte):
        super().__init__(marca, modello, anno, accensione)
        self.__numero_porte=numero_porte

    def suona_clacson(self): #Polimorfismo: attraverso l'override andiamo a specializzare un metodo gia definito nella classe padre
        return "Sto suonando il clacson"
    
class Furgone(Veicolo):

    def __init__(self, marca, modello, anno, accensione,capacita_carico):
        super().__init__(marca, modello, anno, accensione)
        self.__capacita_carico=capacita_carico

    def carica(self,carico):
        pass 

    def scarica(self):
        pass 

class Motocicletta(Veicolo):

    def __init__(self, marca, modello, anno, accensione,tipo):
        super().__init__(marca, modello, anno, accensione)
        self.__tipo=tipo

    def esegui_wheelie(self):
        if self._tipo == "sportiva": return "Eseguo wheelie"
        else: return "Moto non capace"

class GestoreParcoVeicoli:

    def __init__(self):
        self.__veicoli=[]
    

    def get_veicolo(self,veicolo):
        if veicolo in self.__veicoli:
            return Veicolo.stampa(veicolo)
        else: return "Veicolo non presente"
    
    def set_veicolo__marca(self,veicolo,nuovo):
        if veicolo in self.__veicoli:
            return Veicolo.__set__marca(veicolo,nuovo)
        else:
            return "Errore"
    
    def set_veicolo_modello(self,veicolo,nuovo):
        if veicolo in self.__veicoli:
            return Veicolo.__set_modello(veicolo,nuovo)
        else:
            return "Errore"
        
    def get_veicolo__marca(self,veicolo):
        if veicolo in self.__veicoli:
            return Veicolo.__get__marca(veicolo)
        else: return "Veicolo non presente"
    
    def get_veicolo_modello(self,veicolo):
        if veicolo in self.__veicoli:
            return Veicolo.__get_modello(veicolo)
        else: return "Veicolo non presente"

    
    def aggiungi_veicolo(self,veicolo):
        self.__veicoli.append(veicolo)

    def rimuovi_veicolo(self,marca,modello):
     for i in self.__veicoli:
        if Veicolo.__get__marca(i) == marca and Veicolo.__get_modello(i) == modello:
         self.__veicoli.remove(i)
         return "Veicolo rimosso"
        else:
         return "Veicolo non presente"
        
    def lista_veicoli(self):
        for elemento in self._veicoli:
            print(Veicolo.stampa(elemento))


