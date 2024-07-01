#Sto creando dizionario

print("\nCrea un nuovo calciatore")

calciatore={"nome": "nome",
            "cognome": "cognome",
            "eta": 12,
            "sesso": "sesso",
            "ruolo": "ruolo",
}

print(calciatore)
print(type(calciatore))
print(calciatore.get("eta"))
print(calciatore["nome"])

list=[calciatore,10,True]
print(list)
soldi=list[1]
soldi=soldi+1
print(soldi)
#Esercizio lista in dizionario
b=input("Inserisci boolean True/False: ")
n=input("Inserisci un numero intero: ")
s=input("Inserisci una stringa: ")

lis=[b,n,s]

print(lis)

dizi={"nome": "Prova",
      "tipodidato": lis}

print(dizi)


