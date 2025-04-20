"""Escribir una función que reciba una lista de números y devuelva solo aquellos
que son primos. La función debe recibir una lista de enteros 
y retornar solo aquellos que sean primos."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
           39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
           57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
           75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
           93, 94, 95, 96, 97, 98, 99, 100]
print(numeros)
#gracias a copilot por imprimir la lista de prueba
def primos(numeros:list):
    numeros_algunos_primos = []
    numeros_no_todos_primos = []
    numeros_primos = []
    for i in numeros[0:int(len(numeros)):1]: #se usa la estrategia de la raíz
        numeros_no_todos_primos.append(i)
    for j in numeros_no_todos_primos: 
        #se saca una lista con números primos únicos y números no primos repetidos
        for k in range(1,j,1):
            if j % k == 0 and k != j:
                numeros_algunos_primos.append(j)
            else: continue
    for n in numeros_algunos_primos:
        if numeros_algunos_primos.count(n) == 1:
            numeros_primos.append(n)
    return numeros_primos #* esto es posible optimizarlo aún más
if __name__=="__main__":
    print(primos(numeros))