token = True
l=[]
sum=0

while True:
        print("\nMenu:")
        print("1: Ciclo While")
        print("2: Ciclo For")
        print("3. Ciclo Range")
        print("4. Esci")

        seleziona = input("Cosa vuoi fare: ")

        if seleziona=="1":
         while token:
             aggiungi=int(input("Aggiungi un numero: "))
             if aggiungi == 0:
                 token=False
             l.append(aggiungi)
             sum=sum+aggiungi
             n=aggiungi
         
         print("Somma numeri: ",sum)
         
        if seleziona=="2":
         parola=input("Aggiungi una parola: ")
         print("Spelling: ")
         for a in parola:
          print(a)

        if seleziona=="3":
         massimo=int(input("Inserisci il numero di arrivo: "))
         intervallo=int(input("Inserisci un intervallo: "))
         print("Stampa: ")
         for a in range(0,massimo,intervallo):
          print(a)

        if seleziona=="4":
            break
         

                    