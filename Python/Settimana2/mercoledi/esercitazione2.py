"""testo_lipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

#Salviamo il testo in un file chiamato "testo.txt"
with open("testo.txt", "w") as file:
    file.write(testo_lipsum)"""


with open ("testo.txt","r") as file:
    testo_lipsum = file.read()
    
punteggiature = [",", ".", ";", ":"]
slash="\n"
lung = {}
contatore = 0

paroleDuplicate = {}

for punto in punteggiature:
        testo_lipsum = testo_lipsum.lower().replace(punto, "")
        risultato = testo_lipsum.split() 

for i in risultato:
    contatore=contatore+1
    

numero_righe=testo_lipsum.count("\n")

for a in slash:
     nuovo_testo=testo_lipsum.lower().replace(a,"")
     numero_caratteri=len(nuovo_testo)


print("Numero Caratteri: ",numero_caratteri)


print("Numero Righe: ",numero_righe)


print(f"""conteggio parole:
      {paroleDuplicate}""")


print("Parole contate: ",contatore)