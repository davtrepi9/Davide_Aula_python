
class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome=nome
        self.eta=eta
    
    def descrivi(self):
        return f"{self.nome} di {self.eta} fa parte della squadra"

class Giocatore(MembroSquadra):
    
    def __init__(self,nome, eta,ruolo,nmaglia,forma):
        super().__init__(nome, eta)
        self.ruolo=ruolo
        self.nmaglia=nmaglia
        self.forma = forma

    def gioca_partita(self):
        r =  self.ruolo
        if str(r).lower() == "portiere":
            print(f"Parata strepitosa di {self.nome}")
        elif str(r).lower() == "difensore":
            print(f"Intervento chirurgico di {self.nome}")
        elif str(r).lower() == "centrocampista":
            print(f"Sciabolata morbida di {self.nome}")
        elif str(r).lower() == "attaccante":
            print(f"Finalizzazione perfetta di {self.nome}")
        else: print("Errore ruolo giocatore")


class Allenatore(MembroSquadra):
    def __init__(self,nome,eta,anniesperienza,stile):
        super().__init__(nome,eta)
        self.anniesperienza=anniesperienza
        self.stile=stile

    def dirige_allenamento(self):
        s = self.stile
        if str(s).lower() == "tradizionale":
            print(f"Allenamenti duri e fisici, {self.nome} è amante del catenaccio ")
        elif str(s).lower() == "moderno":
            print(f"Allenamenti basati sull'incremento della velocità individuale, {self.nome} è amante del tikitaka")


class Assistente(MembroSquadra):
    def __init__(self, nome, eta,specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
    
    def supporta_team(self):
        sp = self.specializzazione
        if str(sp).lower() == "fisioterapista":
            return f"Forma fisica migliorata"
        elif str(sp).lower() == "analista di gioco":
            return f"Conoscenza tattica migliorata"
        elif str(sp).lower() == "aiuto portiere":
             return f"Overall portiere migliorato"
        

#Si potrebbe pensare di aggiungere e diminuire delle statistiche per ogni giocatore 
#supporta_team potrebbe influire sulle statistiche
#ad ogni gioca partita la forma fisica dei giocatori diminuirebbe
#etc etc (SIMULATORE)



membro1=MembroSquadra("Adolfo",22)
membro2=Giocatore("Totti", 45,"attaccante",10,78)
membro2.gioca_partita()
membro3=Giocatore("Buffon",45,"portiere",1,29)
membro3.gioca_partita()
membro4=Allenatore("Capello",78,20,"tradizionale")
membro4.dirige_allenamento()
print(membro4.descrivi())
membro5=Assistente("Starace",67,"fisioterapista")
print(membro5.supporta_team())

