
class Personaggio:
   
    def __init__(self, username, nome, eta, sesso,corporatura,classe,arma):
        self.__username=username
        self.nome=nome
        self.eta=eta
        self.sesso=sesso
        self.corporatura=corporatura
        self.classe=classe
        self.arma=arma
    
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
    
    def __init__(self, username, nome, eta, sesso,corporatura,classe,arma):
        super().__init__(username, nome, eta, sesso,corporatura,classe,arma)
       

    def attacco_speciale(self):
        return f"AVADAKEDAVRA"

class Barbaro(Personaggio):
    
     def __init__(self, username, nome, eta, sesso,corporatura,classe,arma):
        super().__init__(username, nome, eta, sesso,corporatura,classe,arma)
     
     def attacco_speciale(self):
        return f"VINOOOOOOOOH"
    

class Elfo(Personaggio):
     
     def __init__(self, username, nome, eta, sesso,corporatura,classe,arma):
        super().__init__(username, nome, eta, sesso,corporatura,classe,arma)
       

     def attacco_speciale(self):
        return f"Visione elfica"
     
     def arte_botanica(self):
        return f"Hai ottenuto la capacità di generare pozioni"
    

class Acerrano(Personaggio):
     
     def __init__(self, username, nome, eta, sesso,corporatura,classe,arma):
        super().__init__(username, nome, eta, sesso,corporatura,classe,arma)
       

     def attacco_speciale(self):
        return f"Sono di Æcerr"
     
     def arte_del_wheelie(self,casco):
         if casco:
             return f"Non puoi impennare"
         else: return f"Wheelie Æcerrano effettuato con successo"
         
     
class ElfoAcerrano (Elfo,Acerrano):
     
     def __init__(self, username, nome, eta, sesso,corporatura,classe,arma):
        super().__init__(username, nome, eta, sesso,corporatura,classe,arma)
  

     def attacco_speciale(self):
        return f"Sono di Æcerr in pronvincia di Granburrone"
 


while True:
        print("\nMenu:")
        print("1: Crea Personaggio ")
        print("2: Visualizza Personaggio")
        print("3: NULL")
        print("4: NULL ")
        print("5: Esci ")
    
       
        
        #implementa input utente (per ora testo senza)

        seleziona=input("Cosa vuoi fare: ")
        if seleziona.isalpha():
            print("Errore Input ")
            break
        if seleziona.isspace():
            print("Errore Input ")

        if seleziona =="1":
               
               input_username = input("Inserisci il tuo username: ")
               input_nome = input("Inserisci il nome del tuo personaggio: ")
               input_eta = input("Inserisci l'età del tuo personaggio: ")
               input_sesso = input("Inserisci il sesso del tuo personaggio: ")
               input_corporatura = input("Inserisci la corporatura del tuo personaggio: ")
               input_classe=input("Seleziona Classe (Mago | Barbaro | Elfo | Acerrano | Elfo Acerrano) : ") 
               classe=input_classe.lower()    
               if classe.replace(" ","")=="mago":
                   nuovo_personaggio=Mago(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Bacchetta")
               elif classe.replace(" ","")=="barbaro":
                   nuovo_personaggio=Barbaro(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Ascia")
               elif classe.replace(" ","")=="elfo":
                   nuovo_personaggio=Elfo(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Staffa del bosco")
               elif classe.replace(" ","")=="acerrano":
                   nuovo_personaggio=Acerrano(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Beretta")
               elif classe.replace(" ","")=="elfoacerrano":
                   nuovo_personaggio=ElfoAcerrano(input_username,input_nome,input_eta,input_sesso,input_corporatura,input_classe,"Beretta magica")
               else: print("Errore")
        if seleziona =="2":
            print(Personaggio.visualizza_personaggio(nuovo_personaggio))
        if seleziona =="3":
            pass
        if seleziona =="4":
            pass
        if seleziona =="5":
            break

                


           


