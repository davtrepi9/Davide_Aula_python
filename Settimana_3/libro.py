import random


class Libro:                        

 def __init__(self, titolo,autore):               
    self.titolo = titolo
    self.autore = autore
    self.isbn = random.randint(1,1000)
    #aggiungere controllo su unicità isbn
   
 def descrizione(self):
   return f"Titolo : {self.titolo} - Autore : {self.autore} - ISBN : {self.isbn}"
 
 def nomelibro(self):
    return self.titolo
 
 def valoreisbn(self):
    return self.isbn
 
 
 