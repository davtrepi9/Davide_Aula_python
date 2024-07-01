#Scrivete un programma che riceve in input una stringa lunga e 
# verifica se ci sono duplicati, quanti sono, quali sono e
#quanto sono lunghi i duplicati.
#Esempio:
#‘La casa è grande, una cucina una camera e un giardino. 
#La cucina è piccola e la camera è spaziosa.Il giardino è verde e fiorito.’
#outpout
#"La" appare 2 volte, lunghezza 2.



frase=input("Inserisci una frase: ")
punteggiature =[",",".",";",":"," "]
lung={}

 
def duplicato(frase):
    paroleDuplicate={}

    for punto in punteggiature:
        frase = frase.lower().replace(punto,"")
        risultato=frase.split()
     

    for i in risultato:

    
        val=len(i)
        lung.setdefault(i, val)

        if i not in paroleDuplicate:
            paroleDuplicate[i] = 1

        elif i in paroleDuplicate:
            paroleDuplicate[i] += 1

    
    return paroleDuplicate

print("Occorrenze: ")
print(duplicato(frase))
print("\n")
print("Lunghezza parole: ")
print(lung)