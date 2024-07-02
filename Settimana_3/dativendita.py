class Dati:
    

    
    def __init__(self,day):
        self.day=day   
        self.listadati=[]

    def aggiungi_dati(self):
            d = input("Aggiungi dati separati da spazi: ")
            dsenzaspazi = d.replace(" ","")
            if dsenzaspazi.isnumeric():
             self.listadati=d.split()
            else: print("ERRORE DATI INSERITI")
    
    
    def stampa_lista(self):
        print (f"Giorno: {self.day}")
        print ("Lista dati: %s"  % self.listadati)


    def calcolo_totale(self):
        tot = 0
        for i in self.listadati:
            tot = tot + int(i) 
        return int(tot)
    
    def calcolo_media(self):
        media = 0
        for elemento in self.listadati:
            tot = self.calcolo_totale()
            media= tot // len(self.listadati) 
        return media



#TEST DA SPOSTARE SU MAIN PRINCIPALE
#AGGIUNGERE UN DIZIONARIO CON TUTTI GLI OGGETTI "DATI"

lista = Dati("lunedi")

lista.aggiungi_dati()
lista.stampa_lista()
print(lista.calcolo_totale())
print(lista.calcolo_media())
