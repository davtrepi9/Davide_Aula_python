"""Creare un array unidimensionale con 50 valori compresi tra 1 e 1.000 e dopo dovete eseguire le seguenti operazioni:
- calcolo della media;
- calcolo della deviazione standard;
- trasformarlo in un array 5x10"""

import numpy as np


array = np.random.randint(1, 1001, size= 50)

print(array)

media = array.mean()
devi = array.std()
trasf = array.reshape(5,10)

print("\n Media : ",media)

print("\n Deviazione: ",devi)

print("\n Reshape 5,10 : \n",trasf)
