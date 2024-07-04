
class Personaggio:
   
    def __init__(self, username, nome, eta, sesso,corporatura,classe):
        self.__username=username
        self.nome=nome
        self.eta=eta
        self.sesso=sesso
        self.corporatura=corporatura
        self.classe=classe
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self,nuovo):
        self.nome=nuovo

    def __get_username(self):
        return self.__username
    
    def __set_username(self,nuovo):
        self.__username=nuovo
    
    def visualizza_personaggio(self):
        return f"{self.__username} hai creato:  Nome Unita= {self.nome} - Eta= {self.eta} - Sesso= {self.sesso} - Corporatura= {self.corporatura} - Classe= {self.classe}"

    def attacco_speciale(self):
        return f"Ti sto attaccando"
    
class Mago(Personaggio):
    
    def __init__(self, username, nome, eta, sesso,corporatura,classe,armamagica):
        super().__init__(self, username, nome, eta, sesso,corporatura,classe)
        self.armamagica=armamagica

    def attacco_speciale(self):
        return f"AVADAKEDAVRA"

class Barbaro(Personaggio):
    
     def __init__(self, username, nome, eta, sesso,corporatura,classe,armapesante):
        super().__init__(self, username, nome, eta, sesso,corporatura,classe)
        self.armapesante=armapesante

     def attacco_speciale(self):
        return f"VINOOOOOOOOH"
    

class Elfo(Personaggio):
     
     def __init__(self, username, nome, eta, sesso,corporatura,classe,staffa):
        super().__init__(self, username, nome, eta, sesso,corporatura,classe)
        self.staffa=staffa

     def attacco_speciale(self):
        return f"Visione elfica"
     
     def arte_botanica(self):
        return f"Hai ottenuto la capacità di generare pozioni"
    

class Acerrano(Personaggio):
     
     def __init__(self, username, nome, eta, sesso,corporatura,classe,ferro):
        super().__init__(self, username, nome, eta, sesso,corporatura,classe)
        self.ferro=ferro

     def attacco_speciale(self):
        return f"Sono di Æcerr"
     
     def arte_del_wheelie(self,casco):
         if casco:
             return f"Non puoi impennare"
         else: return f"Wheelie Æcerrano effettuato con successo"
         
     
class ElfoAcerrano (Elfo,Acerrano):
     
     def __init__(self, username, nome, eta, sesso,corporatura,classe,ferroelfico):
        super().__init__(self, username, nome, eta, sesso,corporatura,classe)
        self.ferroelfico=ferroelfico

     def attacco_speciale(self):
        return f"Sono di Æcerr in pronvincia di Granburrone"
 


while True:
        print("\nMenu:")
        print("1: Crea Personaggio ")
        print("2: Visualizza Personaggio")
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
               
               nuovo_personaggio=""
               input_username = input("Inserisci il tuo username: ")
               input_nome = input("Inserisci il nome del tuo personaggio: ")
               input_eta = input("Inserisci l'età del tuo personaggio: ")
               input_sesso = input("Inserisci il sesso del tuo personaggio: ")
               input_corporatura = input("Inserisci la corporatura del tuo personaggio: ")
               input_classe=input("Seleziona Classe (Mago | Barbaro | Elfo | Acerrano | Elfo Acerrano) : ")     
               if input_classe.lower().strip().isalpha()=="mago":
                   nuovo_personaggio=Mago(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Bacchetta")
               elif input_classe.lower().strip().isalpha()=="barbaro":
                   nuovo_personaggio=Barbaro(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Ascia")
               elif input_classe.lower().strip().isalpha()=="elfo":
                   nuovo_personaggio=Elfo(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Staffa del bosco")
               elif input_classe.lower().strip().isalpha()=="acerrano":
                   nuovo_personaggio=Acerrano(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Beretta")
               elif input_classe.lower().strip().isalpha()=="elfoacerrano":
                   nuovo_personaggio=ElfoAcerrano(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Beretta magica")
                   print(nuovo_personaggio.nome)
               else: print("Errore")
        if seleziona =="2":
            pass

                


           



        """
        if seleziona =="2":

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
        break"""

