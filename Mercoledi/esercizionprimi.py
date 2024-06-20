
contatore = 0

def numeroprimo (n,contatore):
 
 for k in range(2,n):
  if (n%k==0):
   print("Il numero non è primo ")
   break
  else:
     print("Il numero è primo!")
     contatore=contatore+1
     
     break
 return contatore

while True:
    numero=int(input("\nInserisci numero da analizzare: "))
    if numero>1:
        contatore=numeroprimo(numero,contatore)
        if contatore==5:
            print("\n --FINITO--")
            break
    elif numero==2:
       print("\nIl numero non è primo")
    else:
       print("\nIl numero non è primo")

 

     

