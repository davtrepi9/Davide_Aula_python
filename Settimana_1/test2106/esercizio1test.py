contatore=0

inp=input("Inserisci una stringa: ")
for i in inp:
 if (i=="a" or i=="e" or i=="i" or i =="o" or i=="u"):
     contatore=contatore+1
print("Numero vocali trovate: ",contatore)