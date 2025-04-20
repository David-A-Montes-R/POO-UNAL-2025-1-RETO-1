"""Escribir una función que reciba una lista de números enteros y 
retorne la mayor suma entre dos elementos consecutivos."""
#lista de prueba ordenada
import random
"""numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
           39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
           57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
           75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
           93, 94, 95, 96, 97, 98, 99, 100]"""
#lista de prueba en desorden
numeros = [42, 7, 99, 18, 65, 23, 81, 54, 36, 12, 91, 3, 76, 47, 25, 88, 58, 1, 33, 100, 
           9, 85, 29, 62, 14, 50, 72, 95, 39, 6, 20, 68, 31, 83, 11, 45, 97, 26, 63, 4, 
           78, 22, 93, 48, 16, 70, 35, 87, 2, 56, 10, 40, 66, 28, 8, 74, 19, 53, 90, 5, 
           32, 60, 13, 84, 46, 24, 98, 37, 17, 67, 30, 80, 44, 15, 71, 34, 92, 49, 21, 
           61, 27, 73, 38, 96, 55, 43, 77, 64, 86, 52, 41, 89, 75, 57, 79, 51, 94, 59, 82, 69, 20]
#lista de prueba muy grande
#numeros = list(range(1, 10000001)) 
#random.shuffle(numeros)  # Mezcla la lista en desorden
def sumador(numeros:list):
    sumas = []
    for n in range(0,len(numeros)-1,1):
        sumas.append(numeros[n]+numeros[n+1]) 
        #se suman todos los números con su consecutivo
    #print(sumas)
    sumas.sort()
    mayor = sumas[len(sumas)-1]
    return mayor
if __name__ == "__main__":
    print("la mayor suma entre dos números consecutivos en la lista es: ")
    print(sumador(numeros))