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

while True:
    print("\nMenu:")
    print("1: Crea ristorante ")
    print("2: Stampa descrizione ")
    print("3: Apri ristorante ")
    print("4: Chiudi ristorante ")
    print("5: Aggiungi piatto al menu ")
    print("6: Elimina piatto dal menu ")
    print("7: Stampa pagina del ristorante ")
    print("8: Esci")

    seleziona=input("Cosa vuoi fare: ")
    if seleziona.isalpha():
      print("Errore Input ")
      break
    if seleziona.isspace():
      print("Errore Input ")

    if seleziona=="1":
     nome=input("Inserisci il nome del ristorante: ")
     tipocucina=input("Inserisci il tipo di cucina: ")
     newr=Ristorante(nome,tipocucina)
    elif seleziona=="2":
     print(newr.descrivi_ristorante())
    elif seleziona=="3":
     print(newr.apri_ristorante())
    elif seleziona=="4":
     print(newr.chiudi_ristorante())
    elif seleziona=="5":
     piatto=input("Inserisci il piatto da aggiungere: ")
     costo=input("Inserisci il costo del piatto: ")
     newr.aggiungi_al_menu(piatto,costo)    
    elif seleziona=="6":
     piatto=input("Inserisci il piatto da eliminare: ")
     costo=input("Inserisci il costo del piatto da eliminare: ")
     newr.togli_dal_menu(piatto,costo)
    elif seleziona=="7":
       print(newr)
    elif seleziona=="8":
       break
    else:
       pass

    

    

