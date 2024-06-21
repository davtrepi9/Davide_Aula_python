token = True
token2 = True
somma = 0



#ripete per 3 volte max
for a in range(3):
    #controllo su input
    while token:
     inp=int(input("Inserisci un numero intero positivo :"))
     if inp<=0:
        print("Errore scelta numero")
        token=True
     else:
        token=False

    #stampa dei numeri pari
    for i in range(1,inp+1,1):
     if i%2==0:
      print(i)
     else:
      somma=somma+i
    #controllo somma
    if somma>250:
      print("SOMMA MAGGIORE 250!\n")
      break
    else:
      token=True

if somma<250:
 print("\nHai finito i tentativi")
     