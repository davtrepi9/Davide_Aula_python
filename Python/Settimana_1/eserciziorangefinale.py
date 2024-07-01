
token = True
n1=0
n2=0


while True:
     print("\n-----MENU----")
     print("1: Pari/Dispari ")
     print("2: Primi in intervallo ")
     print("3. Fattori comuni")
     print("5. Esci ")
     seleziona = input("Cosa vuoi fare: \n")

     #NUMERO1
     
         
     if seleziona=="1":
            print("Cosa vuoi inserire? ")
            print("1: Stringa")
            print("2: Numero ")
            selezion = input("Scrivi(1/2): \n")
            if selezion == "1":
                s = input("Inserisci la stringa: \n")
                n = len(s)
                if n%2==0:
                    print("La stringa è pari ")
                else:
                    print("Stringa dispari")
            elif selezion=="2":
                numero = int(input("Inserisci il numero: \n"))
                if numero%2==0:
                 print("Il numero è pari ")
                else:
                 print("Il numero è dispari ")
            else:
               print("ERROR")
               exit(1)   

     if seleziona=="2":
      n1 = int(input("Inserisci primo valore: \n"))
      n2 = int(input("Inserisci secondo valore: \n"))
      if n1<=n2:
       for i in range(n1,n2,1):
         for k in range(2,i):
             if (i%k==0):
              print(i, ": il numero non è primo ")
              break
             else:
              print(i, ": il numero è primo!")
              break
     if n1>n2:
      for a in range(n1,n2,-1):
         for z in range(2,i):
             if (a%z==0):
              print(a, ": il numero non è primo ")
              break
             else:
              print(a, ": il numero è primo!")
              break
            
      
         
          
          

          