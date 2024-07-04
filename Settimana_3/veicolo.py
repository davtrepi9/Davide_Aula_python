
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

    def get_marca(self):
        return self._marca
    
    def get_modello(self):
        return self._modello
    
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

    
    def aggiungi_veicolo(self,veicolo):
        self._veicoli.append(veicolo)

    def rimuovi_veicolo(self,veicolo):
        self._veicoli.remove(veicolo)

    def lista_veicoli(self):
        for elemento in self._veicoli:
            print(Veicolo.stampa(elemento))


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
    if seleziona =="6":
        parco.rimuovi_veicolo(brum)
        parco.rimuovi_veicolo(motorino)
    if seleziona =="7":
        parco.lista_veicoli()
    if seleziona =="8":
       break

