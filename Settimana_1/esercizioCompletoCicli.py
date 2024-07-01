token = True
somma=0



while True:
        print("\nMenu:")
        print("1: Ciclo While")
        print("2: Ciclo Range")
        print("3. Ciclo For")
        print("4. Stuttura if")
        print("5. Esci")

        seleziona = input("Cosa vuoi fare: ")

        if seleziona=="1":
         while token:
             aggiungi=int(input("Aggiungi un numero: "))
             if aggiungi<=0:
              print("Numero negativo o pari a 0 - ERROR")
              token=True
             else:
              print("Numero accettato")
              token=False

        if seleziona=="2":
         massimo=int(input("Inserisci il numero di arrivo: "))
         for a in range(0,massimo+1,1):
          if a%2==0:
            somma=somma+a
         print(somma)
        
        if seleziona=="3":
         ennesimo=int(input("Aggiungi un numero di arrivo: "))
         print("Numeri dispari: ")
         for n in range(0,ennesimo+1,1):
          if n%2==0:
            pass
          else:
            print(n)
          
        if seleziona=="4":
            nu=int(input("Inserisci un numero maggiore di 1: "))
            nprimo=True 
            for i in range(2,nu):
             if nu%i==0:
              nprimo=False
            if nprimo: #diventa true
              print (nu," è un numero primo")
            else:
              print (nu," non è un numero primo")

        if seleziona=="5":
            break
         
