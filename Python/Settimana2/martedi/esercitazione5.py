#Scrivete un programma che prenda i nomi degli alunni di una
#classe e i loro voti, quando l’utente scrive media il programma
#andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
#media dei voti.
#Esempio:
#Nome: Giovanni , Media: 7.5
#Nome: Alfredo , Media: 9
#Nome: Michela, Media 10
n=0
medie = {},
aula=[]
alunno = {"nome":"",
        "cognome":"",
        "voto1":0,
        "voto2":0,
        "voto3":0}

def inseriscialunno(n):
    v1=input("Inserisci nome: ")
    v2=input("Inserisci cognome: ")
    v3=int(input("Inserisci voto1:" ))
    v4=int(input("Inserisci voto2: "))
    v5=int(input("Inserisci voto3: "))

    alunno.update({"nome":v1})
    alunno.update({"cognome":v2})
    alunno.update({"voto1":v3})
    alunno.update({"voto2":v4})
    alunno.update({"voto3":v5})

    n=n+1
    aula.append(alunno)
    print("Alunno Inserito Correttamente ")
    return aula,alunno

while True:
    print("\nMenu:")
    print("1: Inserisci Alunno")
    print("2: Media")
    print("3: Esci")

    seleziona=input("Cosa vuoi fare: ")
    if seleziona=="1":
     inseriscialunno(n)
     print(alunno)
     print(aula)
    if seleziona=="2":
     for n1 in aula:
       for x in alunno:
         ris = (alunno["voto1"]*alunno["voto2"]*alunno["voto3"])/3
     print(ris)
     

    if seleziona=="3":
     break