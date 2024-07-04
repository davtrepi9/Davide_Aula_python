
class Veicolo:

    def __init__(self,marca,modello,anno,accensione):
        self._marca=marca
        self._modello=modello
        self._anno=anno
        self._accensione=accensione

    def accendi(self):
        self._accensione=True
    
    def spegni(self):
        self.accensione=False
    
    def stampa(self):
        return f"Marca: {self._marca} Modello: {self._modello} Anno: {self._anno} Accensione: {self._accensione}"

    def _get_marca(self):
        return self._marca
    
    def _get_modello(self):
        return self._modello
    
    def __get_anno(self):
        return self._anno
    
    def _set_modello(self,nuovo):
        self._modello=nuovo

    def _set_marca(self,nuovo):
        self._marca=nuovo

    def __set_anno(self,nuovo):
        self._anno=nuovo
    
class Auto(Veicolo):

    def __init__(self, marca, modello, anno, accensione,numero_porte):
        super().__init__(marca, modello, anno, accensione)
        self._numero_porte=numero_porte

    def suona_clacson(self):
        return "Sto suonando il clacson"
    
class Furgone(Veicolo):

    def __init__(self, marca, modello, anno, accensione,capacita_carico):
        super().__init__(marca, modello, anno, accensione)
        self._capacita_carico=capacita_carico

    def carica(self,carico):
        pass #inserisce elemento con append in una lista

    def scarica(self):
        pass #svuota la lista e restituisce il contenuto

class Motocicletta(Veicolo):

    def __init__(self, marca, modello, anno, accensione,tipo):
        super().__init__(marca, modello, anno, accensione)
        self._tipo=tipo

    def esegui_wheelie(self):
        if self._tipo == "sportiva": return "Eseguo wheelie"
        else: return "Moto non capace"

class GestoreParcoVeicoli:

    def __init__(self):
        self._veicoli=[]
    

    def get_veicolo(self,veicolo):
        if veicolo in self._veicoli:
            return Veicolo.stampa(veicolo)
        else: return "Veicolo non presente"
    
    def set_veicolo_marca(self,veicolo,nuovo):
        if veicolo in self._veicoli:
            return Veicolo._set_marca(veicolo,nuovo)
        else:
            return "Errore"
    
    def set_veicolo_modello(self,veicolo,nuovo):
        if veicolo in self._veicoli:
            return Veicolo._set_modello(veicolo,nuovo)
        else:
            return "Errore"
        
    def get_veicolo_marca(self,veicolo):
        if veicolo in self._veicoli:
            return Veicolo._get_marca(veicolo)
        else: return "Veicolo non presente"
    
    def get_veicolo_modello(self,veicolo):
        if veicolo in self._veicoli:
            return Veicolo._get_modello(veicolo)
        else: return "Veicolo non presente"

    
    def aggiungi_veicolo(self,veicolo):
        self._veicoli.append(veicolo)

    def rimuovi_veicolo(self,marca,modello):
     for i in self._veicoli:
        if Veicolo._get_marca(i) == marca and Veicolo._get_modello(i) == modello:
         self._veicoli.remove(i)
         return "Veicolo rimosso"
        else:
         return "Veicolo non presente"
        
    def lista_veicoli(self):
        for elemento in self._veicoli:
            print(Veicolo.stampa(elemento))




#TESTING COMPLETATO / CREARE MENU CON INPUT UTENTE

while True:
    print("\nMenu:")
    print("1: Nuovo veicolo ")
    print("2: Accendi veicolo")
    print("3: Spegni veicolo ")
    print("4: Visualizza veicolo ")
    print("5: Inserisci veicolo nel Parco ")
    print("6: Rimuovi veicolo dal Parco")
    print("7: Lista veicolo dal Parco")
    print("8: ESCI")
      
      #implementa input utente (per ora testo senza)

    seleziona=input("Cosa vuoi fare: ")
    if seleziona.isalpha():
         print("Errore Input ")
         break
    if seleziona.isspace():
        print("Errore Input ")

    if seleziona =="1":
        #implementa altro mini menu interno per scegliere che veicolo creare
        brum = Auto("Ford","Fiesta",2018,True,5)
        furgoncino = Furgone("Cristiano","Malgioglio",1950,False,30)
        motorino = Motocicletta("CesareCremonini","Vespa50",2000,True,"Sportiva")
    if seleziona =="2":
        furgoncino.accendi()
    if seleziona =="3":
        brum.spegni()
    if seleziona =="4":
        print(brum.stampa())
        furgoncino.stampa()
    if seleziona =="5":
        parco=GestoreParcoVeicoli()
        parco.aggiungi_veicolo(brum)
        parco.aggiungi_veicolo(furgoncino)
        parco.aggiungi_veicolo(motorino)
        print(parco.get_veicolo(brum))
    if seleziona =="6":
        print(parco.get_veicolo_marca(brum))
        print(parco.get_veicolo_modello(furgoncino))

        parco.set_veicolo_marca(brum,"Porsche")
        parco.set_veicolo_modello(brum,"DALAILAMA")

        print(parco.get_veicolo(brum))
       
        print(parco.rimuovi_veicolo("Porsche","DALAILAMA"))
        print(parco.rimuovi_veicolo("Ciao","Mamma"))

    if seleziona =="7":
        parco.lista_veicoli()
    if seleziona =="8":
       break

