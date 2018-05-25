# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

#Creo un rango muy grande, para correr multiples veces el codigo.
for i in range (100000)
#Para cada iteracion del codigo calculo un x, que sera un numero aleatorio.
  x= np.int_(np.random.random(100)*1000)
#Si el numero es impar entonces lo imprimo
  if (x%2!=0):
    print x
#Si el numero es superior a 800 creo un break para romper el ciclo del for.
  if (x>800):
    break



