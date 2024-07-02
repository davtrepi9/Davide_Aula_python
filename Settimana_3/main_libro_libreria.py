import libro
import libreria


nlibro = libro.Libro("Titologenerico","Autoregenerico")
nlibro2 = libro.Libro("Titologenerico22","Autoregenerico22")

print(nlibro.descrizione())
print(nlibro2.descrizione())

nlibreria = libreria.Libreria()
nlibreria.aggiungi_libro(nlibro)
nlibreria.aggiungi_libro(nlibro2)
print(nlibreria.mostra_catalogo())
print(nlibreria.rimuovi_libro(nlibro2))
print(nlibreria.mostra_catalogo())
nlibreria.cerca_per_titolo("Titologenerico22")
