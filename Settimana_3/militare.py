class UnitaMilitare:
   
    def __init__(self, nome, numero_soldati):
        self.nome=nome
        self.numero_soldati=numero_soldati
    
    def get_nome(self):
        return self.nome
    
    def get_numero(self):
        return self.numero_soldati
    
    def __str__(self):
     return f" Nome Unita: {self.nome} - Numero Soldati: {self.numero_soldati}"

    def muovi(self):
        return f"Unità {self.nome} in movimento"
    
    def attacca(self):
        return f"Unità {self.nome} procede all'attacco"
    
    def ritira(self):
        return f"Unità {self.nome} in ritirata"

    def tipo(self):
        return type(self)
    
class Fanteria(UnitaMilitare):
    
    def __init__(self,nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        

    def costruisci_trincea(self):
        trincea=True
        return trincea,f" Unità {self.nome} ha costruito la trincea" 

class Artiglieria(UnitaMilitare):
    
    def __init__(self,nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def calibra_artiglieria(self):
        x=input("Inserisci ascissa x: ")
        y=input("Inserisci ordinata y: ")
        calibra=x+","+y
        return calibra,f" Unità {self.nome} ha calibrato su coordinate {x} , {y}"    

class Cavalleria(UnitaMilitare):
    
    def __init__(self,nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def esplora_terreno(self):
        p = input("In che posizione deve esplorare (sud/est/nord/ovest): ")
        if p.lower() == "sud" or p.lower() == "est" or p.lower() == "nord" or p.lower() == "ovest":
         return p,f" {self.muovi()} verso {p}"
        else: print("Errore posizione")
    
class SupportoLogistico(UnitaMilitare):
    
    def __init__(self,nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        

    def rifornisci_unita(self):
        pass

class Ricognizione(UnitaMilitare):

    def __init__(self,nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        
    def conduci_ricognizione(self):
        pass

class ControlloMilitare(Fanteria,Artiglieria,Cavalleria,SupportoLogistico,Ricognizione):

    unitaregistrate={}
    def __init__(self,nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        
        
    def registra_unita(self,unita):
        numero = UnitaMilitare.get_numero(unita)
        unita = UnitaMilitare.get_nome(unita)
        
        self.unitaregistrate[unita]=numero

    def mostra_unita(self):
        return self.unitaregistrate.items()
    
    def dettagli_unita(self,nome):
        if nome in self.unitaregistrate:
            return f"{nome} e stampa descrizioni e cose varie"
        

#TESTING

generico = UnitaMilitare("Generico",10)
print(generico)

fanteria = Fanteria("Fantini",20)
print(fanteria)
print(fanteria.costruisci_trincea())

artiglieria = Artiglieria("Artigli",12)
print(artiglieria)
print(artiglieria.calibra_artiglieria())

cavalleria = Cavalleria("Cavalli",30)
print(cavalleria)
print(cavalleria.esplora_terreno())

controllomilitare=ControlloMilitare("Controllo militare",5)
print(controllomilitare)
controllomilitare.registra_unita(cavalleria)
controllomilitare.registra_unita(fanteria)
print(controllomilitare.mostra_unita())
print(controllomilitare.dettagli_unita("Fantini"))