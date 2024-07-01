#Scrivete un programma che chiede un numero all’utente e
#restituisce un dizionario con il quadrato del numero, se è pari o
#dispari e quante cifre contiene.
#Esempio:
#Numero 12
#Risultato
#{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }
token=True
dizio={"quadrato":0,
       "pari o dispari":"",
       "n.cifre":0}
while token:
    inp=input("Inserisci un numero: ")
    if inp.isalpha():
       print("ERROR INPUT NON VALIDO")
       exit(1)
    #quadrato
    dizio["quadrato"]=int(inp)*int(inp)
    #pariodispa
    if int(inp)%2==0:
        dizio["pari o dispari"]="pari"
    else:
        dizio["pari o dispari"]="dispari"
    #numerocifre
    dizio["n.cifre"]=len(str(inp))

    print(dizio)
    scelta=(input("Vuoi ripetere?(si/no): "))
    if scelta.lower()=="si":
     token=True
    elif scelta.lower()=="no":
     token=False
    else:
     print("ERRORE INPUT NON VALIDO")
     exit(1)