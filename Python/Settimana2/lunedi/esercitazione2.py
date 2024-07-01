#Scrivete una programma che richiede una lista di numeri all’utente e 
#fornisce in output un istogramma basato su questi numeri, usando asterischi
#per disegnarlo.
#Data ad esempio la lista [3, 7, 9, 5], il programma dovrà produrre questa
#sequenza:*** ******* ********* *****

lista=[]
token=True
istogramma=[]
elemento=""

while token:
    inp=(input("Inserisci un valore o scrivi ESCI per uscire: "))
    if inp.upper()=="ESCI":
     token=False
    elif inp.isdecimal():
     if int(inp)<=0:
       print("ERROR input not valid ")
     else:
      lista.append(int(inp))
    else:
     print("ERROR")
     exit(1)

for x in lista:
  elemento="*"*(x)
  istogramma.append(elemento)

print("Istogramma: ")
for n in istogramma:
  print(n)