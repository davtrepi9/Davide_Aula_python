

class Animale:
    def __init__(self, nome, età):
        self.nome=nome
        self.età=età
    
    def fai_suono(self, suono):
        print(suono)

class Leone(Animale):
    def __init__(self, nome, età):
        Animale.__init__(self,nome, età)

    def fai_suono(self):
        print("ROAR")
    
    def caccia(self):
        print("HUNTER HUNTER")

class Pinguino(Animale):
    def __init__(self, nome, età):
        super().__init__(nome, età)
    
    def get_Eta(self):
        return self.età
    
    def fai_suono(self):
        print("NGUE NGUE")


a=Animale("animale",12)
leo=Leone("Gianpaolo", 9)
leo.fai_suono()
leo.caccia()
pingu=Pinguino("Armando", 11)
print(pingu.get_Eta())