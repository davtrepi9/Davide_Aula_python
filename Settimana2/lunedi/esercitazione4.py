#Scrivete un programma che chiede un numero all’utente e
#restituisce un dizionario con il quadrato del numero, se è pari o
#dispari e quante cifre contiene.
#Esempio:
#Numero 12
#Risultato
#{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }

dizio={"quadrato":0,
       "pari o dispari":"",
       "n.cifre":0}

inp=int(input("Inserisci un numero: "))

#quadrato
dizio["quadrato"]=inp*inp
#pariodispa
if inp%2==0:
    dizio["pari o dispari"]="pari"
else:
    dizio["pari o dispari"]="dispari"
#numerocifre
dizio["n.cifre"]=len(str(inp))

print(dizio)