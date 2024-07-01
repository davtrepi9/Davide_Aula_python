
token = True
token2 = True
somma = 0
contatore=0

#controllo su input
while token2:
    while token:
     inp=int(input("Inserisci un numero intero positivo :"))
     if inp<=0:
        print("Errore scelta numero")
        token=True
     else:
        token=False

    contatore=contatore+1

    #stampa dei numeri pari
    for i in range(0,inp+1,1):
     if i%2==0:
      print(i)
     else:
      somma=somma+i
    
    token=False

    if somma>250:
      print("SOMMA MAGGIORE 250!\n")
      token2: False
      token: False
    elif contatore==3:
      print("Tentativi esauriti! \n")
      token2: False
      token: False


  

 