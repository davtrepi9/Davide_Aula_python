def fibonacci(n):
    if n<0:
        print("ERROR")
        return False
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



numero=int(input("Inserisci un numero limite: "))
for i in range(1, numero+1):
 print(fibonacci(i))
