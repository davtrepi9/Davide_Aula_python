
class Posto:
        def __init__(self, numero, fila,occupato):
         self.__numero=numero
         self.__fila=fila
         self.__occupato=occupato

        def prenota(self):
            if self.__occupato==False:
                self.__occupato=True
            else:
                return f"Posto già occupato"
        
        def libera(self):
            if self.__occupato==True:
                self.occupato=False
            else:
                return f"Posto già libero"
            
        def get_numeri(self):
            return self.__numero
    
        def get_fila(self):
            return self.__fila

        def statoposto(self):
            if self.__occupato:
                return True
            else: return False

class PostoVIP(Posto):

    def __init__(self, numero, fila,occupato,servizi_extra):
     super().__init__(numero, fila,occupato)
     self.__servizi_extra=servizi_extra

    def prenota(self):
     if self.__occupato==False:
      self.__occupato=True
      print(f"Hai diritto a {self.__servizi_extra}")
     else: print("Posto già occupato")

    def costoaggiuntivo(self):
        pass

class Teatro():

    def __init__(self):
        self._posti=[]
    
    def modifica_posto(self,nuovo):
        self._posti=nuovo
    def inserisci_posti(self,posto):
        self._posti.append(posto)
       
    def prenota_posto(self,numero,fila):
        for i in self._posti:
            if numero == Posto.get_numeri(i) and fila == Posto.get_fila(i):
                Posto.prenota(i)
                self.modifica_posto(i)
    
    def stampa_posti_occupati(self):
        for i in self._posti:
            stato=Posto.statoposto(i)
            if stato == True:
                print(f"Fila: {Posto.get_fila(i)} Numero: {Posto.get_numeri(i)} è occupato")
            


x=Posto("3","2",True)
posto2=Posto("1","2",False)
posto3=Posto("15","1",True)
posto4=Posto("10","3",False)

t = Teatro()

t.inserisci_posti(x)
t.inserisci_posti(posto2)
t.inserisci_posti(posto3)
t.inserisci_posti(posto4)

t.stampa_posti_occupati()