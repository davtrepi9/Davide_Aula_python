
class Prodotto:                        
 
 def __init__(self, nome,costo_produzione,prezzo_vendita):               
    self.nome = nome
    self.costo_produzione = costo_produzione
    self.prezzo_vendita = prezzo_vendita
   
 def __str__(self):
   return f" Nome prodotto: {self.nome} -  Costo Produzione: {self.costo_produzione} - Prezzo Vendita: {self.prezzo_vendita} "
 
 def calcola_profitto(self):
   profitto=self.prezzo_vendita-self.costo_produzione
   return f"Profitto: {profitto}"
 
 def nomeprodotto(self):
   return self.nome

class Elettronica:
  
 def __init__(self,garanzia):
   self.garanzia=garanzia


class Abbigliamento:
  
 def __init__(self,materiale):
   self.materiale=materiale


class Fabbrica:

 inventario={}

 def aggiungi_prodotto(self,prodotto,quantita):
  prodotto = Prodotto.nomeprodotto(prodotto)
  self.inventario[prodotto]=quantita
 
 def stampa_inv(self):
   return self.inventario.items()

 def vendi_prodotto(self,prodotto):
   nprodotto = Prodotto.nomeprodotto(prodotto)
   if nprodotto in self.inventario.keys():
    profitto = Prodotto.calcola_profitto(prodotto)
    del self.inventario[nprodotto]
    return profitto
   else: return f"Prodotto non presente"
   
 def resi_prodotto(self,prodotto):
    nprodotto = Prodotto.nomeprodotto(prodotto)
    if nprodotto in self.inventario.keys():
        nuovaquantita = self.inventario[nprodotto]
        nuovaquantita = nuovaquantita + 1
        self.inventario={nprodotto : nuovaquantita}
        return f"Prodotto aggiunto con successo"
    else: return f"Prodotto non presente"
    

#MAIN
#Creo nuovo prodotto generico
newp=Prodotto("Camicia",3,13)
#Stamp nuovo prodotto
print(newp)
#Calcolo profitto prodotto
print(newp.calcola_profitto())

#Creo nuova fabbrica
newf=Fabbrica()
#Aggiungo prodotto all'inventario della fabbrica
newf.aggiungi_prodotto(newp,5)
#Stampo inventario fabbrica
print(newf.stampa_inv())
#Resto prodotto fabbrica
print(newf.resi_prodotto(newp))
#Stampo inventario fabbrica
print(newf.stampa_inv())
#Vendita prodotto fabbrica
print(newf.vendi_prodotto(newp))
#Stampo inventario fabbrica
print(newf.stampa_inv())
