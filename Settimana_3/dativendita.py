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
    
    def stampa_media(self):
        return "Lista media: %s"  % listamedia


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
        listamedia.append(media) 
        return media
    
    def calcolo_totale2(self):
        tot2 = 0
        for i in listamedia:
            tot2 = tot2 + int(i) 
        return int(tot2)
    
    def sopra_la_media(self):
        mediatot = 0
        for elemento in listamedia:
            tot2 = self.calcolo_totale2()
            mediatot = tot2 // len(listamedia)

1



#TEST DA SPOSTARE SU MAIN PRINCIPALE
#AGGIUNGERE UN DIZIONARIO CON TUTTI GLI OGGETTI "DATI"
listamedia=[]

lista = Dati("lunedi")
lista2 = Dati("martedi")

lista.aggiungi_dati()
lista.stampa_lista()
print(lista.calcolo_totale())
print(lista.calcolo_media())
print(lista.stampa_media())

lista2.aggiungi_dati()
lista2.stampa_lista()
print(lista2.calcolo_totale())
print(lista2.calcolo_media())
print(lista2.stampa_media())



print(lista.sopra_la_media())
