
lista=[]
x = 0

while True:
    print("\nMenu:")
    print("1: Aggiungi")
    print("2: Rimuovi")
    print("3. Visualizza")
    print("4. Esci")

    seleziona = input("Cosa vuoi fare: ")

    if seleziona =="1":
        add = input("Inserisci valore: ")
        lista.insert(x,add)
    elif seleziona =="2":
        add = input("Inserisci cosa vuoi rimuovere: ")
        lista.remove(add)
    elif seleziona =="3": 
        print(lista)
    elif seleziona =="4":
        break

