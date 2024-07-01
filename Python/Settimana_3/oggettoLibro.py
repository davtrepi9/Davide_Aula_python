
class Libro:                         # dichiaro la classe
 
 def __init__(self, titolo,autore,pagine):               # metodo di istanza
    self.__titolo = titolo
    self.__autore = autore
    self.__pagine = pagine
   
    
 def __str__(self):
    return f'Il libro {self.__titolo} è stato scritto da {self.__autore} e ha {self.__pagine} pagine.'
 


nuovolibro = Libro("1984","Orwell","120")
print(nuovolibro)


