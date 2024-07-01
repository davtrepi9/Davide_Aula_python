token = True
somma=0
l=[]
lprimi=[]
sommap=0

from random import *

while True:
        print("\nMenu:")
        print("1: Check Positivo")
        print("2: Lista Random")
        print("3. Somma Lista")
        print("4. Stampa dispari lista")
        print("5. Numero primo")
        print("6. Stampa numeri primi")
        print("7. Somma numeri se primo")
        print("8. Esci")

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
         for a in range(1,massimo+1,1):
          x=randint(1,massimo)
          l.append(x) 
         print(l)
         
        if seleziona=="3":
         print("La somma è : ")
         for a in l:
          if a%2==0:
            somma=somma+a
          else:
            pass
         print(somma)
          
        if seleziona=="4":
         print("Numeri dispari: ")
         for a in l:
          if a%2==0:
           pass
          else:
            print(a)
            
        if seleziona=="5":
            nu=int(input("Inserisci un numero maggiore di 1: "))
            nprimo=True 
            for i in range(2,nu):
             if nu%i==0:
              nprimo=False
            if nprimo: #diventa true
              print (nprimo)
            else:
              print (nprimo)
       
       #non funziona
        if seleziona=="6":
           nnprimo=True
           for x2 in l:
            for i in range(1,x2):
             if x2%i==0:
              nnprimo=False
            if nnprimo: #diventa true
              lprimi.append(x2)
              break
            else:
              pass
              
           print("Numeri primi lista: ")
           print(lprimi)
       
        if seleziona=="7":
          for d in l:
           sommap=sommap+d
          j=True 
          for i in range(1,sommap):
           if sommap%i==0:
             j=False
           if j: #diventa true
             print (sommap," è un numero primo")
           else:
             print("Non è primo")
            

        if seleziona=="8":
            break
         
