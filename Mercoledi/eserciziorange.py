
 
numero=0

def finalcountdown(numero):
    print("\n")
    for i in range(numero,0,-1):
        print(i)
    scelta=input("\nVuoi continuare?: ")
    if scelta=="si":
       start()
    elif scelta=="no":
        print("\nCHIUSURA")
        return(False)
    else:
       print("\nERROR")
       exit(1)
    
        


def start():
    num = int(input("\nInserisci un numero di partenza: "))
    if num<0:
     print("\nErrore numero inferiore a 0")
     exit(1)
    else:
        while True :
         if finalcountdown(num) == False:
            break


print("BENVENUTO")
start()

         




