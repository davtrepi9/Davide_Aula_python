
#Sto creando tupla
print("\nStampa tupla")
x=("a","b","c")
print(x)

#Tuple packing
print("\nStampa milan tuple packing")
milan="Maldini","Gattuso","Kakà"
dif,cen,atk = milan
print(dif,cen)

print("\nStampo il tipo")
#Stampo il tipo
print(type(x))

print("\nStampo la lunghezza")
#Stampo lunghezza
print(len(x))

print("\nControllo sulla presenza di un elemento")
#Controllo sulla presenza
richiesta=input("Che vuoi controllare?: ")
if(richiesta in milan):
    print("Tranquillo ci sta")
else:
    print("Nada")


