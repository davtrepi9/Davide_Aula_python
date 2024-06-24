#Scrivete un programma che chiede una stringa all’utente e
#restituisce un dizionario rappresentante la "frequenza di
#comparsa" di ciascun carattere componente la stringa.
#Esempio:
#Stringa "ababcc",
#Risultato
#{"a": 2, "b": 2, "c": 2}

dizio={}
inp=input("Inserisci una stringa: ")

for x in inp.lower():
    if x==" ":
     pass
    else:
     dizio.setdefault(x, 0)
     dizio[x] = dizio[x] + 1

print("Frequenza di comparsa: ")
print(dizio)