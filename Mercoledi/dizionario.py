#Sto creando dizionario

print("\nCrea un nuovo calciatore")
nome=input("Inserisci nome: ")
cognome=input("Inserisci cognome: ")
eta=input("Inserisci eta: ")
sesso=input("Inserisci sesso: ")
ruolo=input("Inserisci ruolo: ")

calciatore={"nome": nome,
            "cognome": cognome,
            "eta": eta,
            "sesso": sesso,
            "ruolo": ruolo,
}
print(calciatore)
print(type(calciatore))
print(calciatore.get("eta"))

#Esercizio lista in dizionario
b=input("Inserisci boolean True/False: ")
n=input("Inserisci un numero intero: ")
s=input("Inserisci una stringa: ")

lis=[b,n,s]

print(lis)

dizi={"nome": "Prova",
      "tipodidato": lis}

print(dizi)

