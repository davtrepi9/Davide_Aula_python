import libro

class Libreria:
    
    catalogo={}
    

    def aggiungi_libro(self,lib):
     l = libro.Libro.nomelibro(lib)
     i = libro.Libro.valoreisbn(lib)
     self.catalogo[l] = str(i)

    def rimuovi_libro(self,lib):
     l = libro.Libro.nomelibro(lib)
     i = libro.Libro.valoreisbn(lib)
     if str(i) in self.catalogo.values():
        del self.catalogo[l]
        return f"Libro rimosso dal catalogo"
     else: return f"Libro non presente"

    def cerca_per_titolo(self,l):
      if l in self.catalogo.keys():
        print(l)
      
    def mostra_catalogo(self):
     return self.catalogo.items()
        
