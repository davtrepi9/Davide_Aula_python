#Programma che chiede all'utente una lista di parole 
#e restituisce la lunghezza di ogni parola

lista=[]
token=True

while token:
 inp=(input("Inserisci una parola: "))
 lista.append(inp)
 scelta=input("Vuoi continuare?(si/no): ")
 if scelta=="si":
  pass
 else:
  token=False

for x in lista:
 print(len(x))

