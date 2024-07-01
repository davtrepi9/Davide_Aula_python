#Classe Ristorante che gestisce alcune funzionalità
#Requisiti:
#Definizione della classe: __init__ che accett aude parametri, nome e tipo cucina
#Definire un attributo aperto che indica se il ristorante è aperto o chiuso (False default)
#Un dizionario menu dove dentro ci sono i piatti a prezzi che ha il ristorante
#METODI:


class Ristorante:   
                      
 aperto = False
 menu=[]

 def __init__(self, nome,tipo_cucina):               
        self.nome = nome
        self.tipo_cucina = tipo_cucina

 def __str__(self):
    return f"Nome ristorante: {self.nome} -  Tipo Cucina: {self.tipo_cucina} - Aperto: {self.aperto} -  Menu: {self.menu} "
 
 def descrivi_ristorante(self):
    return f"Seminascosto nei pressi di Porta Romana, {self.nome} è un locale intimo e accogliente, che propone un piccolo menu di piatti ispirati al tipo di cucina {self.tipo_cucina} interpretati con fantasia e attenzione."

 def stato_apertura(self):
      if self.aperto==False:
           return f"Ristorante chiuso"
      else:
           return f"Ristorante aperto"
 
 def apri_ristorante(self):
      self.aperto=True
      return self.stato_apertura()

 def chiudi_ristorante(self):
      self.aperto=False
      return self.stato_apertura()

 def aggiungi_al_menu(self,piatto,costo):
        piattonuovo=str(piatto)+","+str(costo)
        self.menu.append(piattonuovo)
 
 def togli_dal_menu(self,piatto):
      self.menu.remove(piatto)
     

    
#TESTING 

newr=Ristorante("CaboInn","Mexican")

print(newr.descrivi_ristorante())

print(newr.apri_ristorante())

print(newr.chiudi_ristorante())

newr.aggiungi_al_menu("Morgan","3")

newr.aggiungi_al_menu("Per","10")

print(newr)

newr.togli_dal_menu("Morgan,3")

print(newr)