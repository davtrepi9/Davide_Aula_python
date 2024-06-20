#variabili
token=True
lista1=[]
listaq=[]
lista2=[]
contatore=0
massimo=0
#menu
while True:
     print("\n-----MENU----")
     print("1: Pari/Dispari ")
     print("2: Countdown ")
     print("3. Quadrato degli elementi di una lista")
     print("4. Max di una lista e conteggio ")
     print("5. Esci ")
     seleziona = input("Cosa vuoi fare: \n")
    
    #NUMERO1
     if seleziona=="1":
        valore1 = int(input("\nInserire il numero: "))
        if valore1==0:
           print("\nValore pari a zero")
        elif valore1%2==0:
           print("PARI\n")
        else:
           print("DISPARI\n")
     

    #NUMERO 2
     if seleziona=="2":
        while token:
         valore2 = int(input("\nInserire il numero: "))
         for i in range(valore2,0,-1):
            print(i)
         scelta = input("\nVuoi continuare ? (si/no)")
         if scelta == "no":
            token=False
         if scelta == "si":
            token=True
               
               
    #NUMERO 3  
     if seleziona=="3":
      while True:
        seleziona = input("Vuoi aggiungere un elemento?: ")
        if seleziona == "si":
         valore4 = int(input("Inserire il numero da inserire: "))
         lista1.append(valore4)
        elif seleziona == "no":
         break     
      print("Lista creata: ",lista1)
      for i in lista1:
        quadrato=i*i
        listaq.append(quadrato)
      print("Lista quadrata: ",listaq)

    
    #NUMERO 4
     if seleziona=="4":
        while True:
         seleziona = input("Vuoi aggiungere un elemento?: ")
         if seleziona == "si":
          valore4 = int(input("Inserire il numero da inserire: "))
          lista1.append(valore4)
          contatore=contatore+1
         elif seleziona == "no":
          break
        if len(lista1)==0:
         print("Lista Vuota")
        else: 
         print("Lista creata: ",lista1)
         for i in lista1:
          if massimo<i:
           massimo=i
         print("Massimo: ",massimo)
         print("Numero elementi lista: ",contatore)
        

     if seleziona=="5":
        break

     



     
     

            
            
     
