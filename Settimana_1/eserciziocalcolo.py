#Descrizione: Scrivi un programma che chieda all'utente di inserire due numeri e 
#un'operazione da eseguire tra addizione (+), sottrazione (-), moltiplicazione (*) e divisione (/). 
#Il programma dovrebbe poi eseguire l'operazione e stampare il risultato. 
#Tuttavia, se l'utente tenta di dividere per zero, il programma dovrebbe stampare "Errore: Divisione per zero".
#Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione non valida".

n1= input("Inserisci il primo numero : ")
n2= input("Inserisci il secondo numero :")
n3=0

while True:
    print("\n-----Operazioni disponibili----")
    print("1: + ")
    print("2: - ")
    print("3. * ")
    print("4. / ")
    print("5. Esci ")
    seleziona = input("Cosa vuoi fare: ")

    if seleziona =="1":
        n3=int(n1)+int(n2)
        print("\nIl risultato e': ",n3)
    elif seleziona =="2":
         n3=int(n1)+int(n2)
         print("\nIl risultato e': ",n3)
    elif seleziona =="3": 
        n3=int(n1)*int(n2)
        print("\nIl risultato e': ",n3)
    elif seleziona =="4":
        if(int(n2)==0):
            print("\nErrore, secondo valore uguale a 0")
            break
        else :
            n3=int(n1)/int(n2)
        print("\nIl risultato e': ",n3)
    elif seleziona =="5":
        break
    else:
        print("\nOperazione non valida")
