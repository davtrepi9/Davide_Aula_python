
class Libro:                        
 
 def __init__(self, titolo,autore,pagine):               
    self.titolo = titolo
    self.autore = autore
    self.pagine = pagine
   
 def __str__(self):
   return f"{self.titolo}"
 
 def nomelibro(self):
    return self.titolo
 

class Biblioteca:
    
    listalibri=[]
    
    def aggiungi_libro(self,libro):
     libro = Libro.nomelibro(libro)
     self.listalibri.append(libro)

    def stampa_libri(self):
        for i in self.listalibri:
           print(i)



biblio = Biblioteca()
for i in range(2):
    titolo = input("Inserisci Titolo: ")
    autore = input("Inserisci Autore: ")
    pagine = input("Inserisci Numero pagine: ")
    nuovolibro = Libro(titolo,autore,pagine)
    biblio.aggiungi_libro(nuovolibro)
 

    
        
biblio.stampa_libri()


