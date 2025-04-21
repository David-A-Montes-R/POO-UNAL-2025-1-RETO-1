# RETO 1 POO

En este reto se busca recuperar algunos conceptos de programación estructurada con Python antes de entrar a los conceptos de la programación orientada a objetos, por lo que se realizan diferentes algoritmos que realizan diferentes tareas:

## Punto 1

*Crear una función que realice operaciones básicas 
(suma, resta, multiplicación, división) entre dos números, 
según la elección del usuario, la forma de entrada 
de la función será los dos operandos y el caracter usado para la operación. 
entrada: (1,2,"+"), salida (3).*

Para realizar este ejercicio se crea un programa que recibe sucesivamente 3 inputs y luego realizas las operaciones correspondientes según un **match case** del último input que es el que define la operación. Previo al ingreso de este input se imprime una guía de operaciones para el usuario. Como característica particular de este programa se incluye también la potencia y se importa **time** para poder imprimir la guía.

```python
import time
def operaciones(n:float,m:float,op:str):
    match op:
        case "+":
            resultado = n + m
        case "*":
            resultado = n * m
        case "-":
            resultado = n - m
        case "/":
            resultado = n / m
        case "^":
            resultado = n ** m
        case _:
            resultado = "vuelva a introducir el símbolo operativo ( +,-,*,/,^) "        
    return resultado
if __name__ == '__main__':
    n = float(input("introduzca el primer número: "))
    m = float(input("introduzca el segundo número: "))
    print("guía de símbolos:")
    time.sleep(1)
    print( "suma: +","\n", "resta:-","\n", "multiplicación : *","\n",
          "division: /","\n","potencia: ^")
    op = str(input("introduzca la operación que quiere realizar(símbolo): "))
    print("resultado:",operaciones(n,m,op))
```
## Punto 2

*Realice una función que permita validar si una palabra es un palíndromo. 
Condición: No se vale hacer slicing para invertir la palabra y verificar 
que sea igual a la original.*

En este caso, dado que no se permite aplicar el slicing a las cadenas de entrada, estas cadenas se descomponen mediante un bucle **for** en carácteres, y se crea una lista en dónde empleando otro bucle **for** sobre la primera lista creada, el cual recorre la lista en sentido inverso, crea otra lista, la cual luego se compara con la primera. Si estas listas resultan iguales, la palabra será un palíndromo.(Técnicamente esto sería una versión de slicing DIY)

```python
def palíndromo(palabra:str):
    lista_caracteres = []
    lista_caracteres_2 = []
    for ch in palabra:
        lista_caracteres.append(ch)
    for i in range(len(lista_caracteres),0,-1):
        lista_caracteres_2.append(lista_caracteres[i-1])
#* monitorización
    #print(lista_caracteres)
    #print(lista_caracteres_2)
    if lista_caracteres == lista_caracteres_2:
        juicio = True
    else:
        juicio= False
    return juicio
if __name__ == "__main__":
    palabra = str(input("introduzca la palabra para saber si es palíndromo o no:"))
    if palíndromo(palabra) == True:
        print("la palabra introducida es un palíndromo")
    else:
        print("la palabra no es un palíndromo")
```

## Punto 3

*Escribir una función que reciba una lista de números y devuelva solo aquellos
que son primos. La función debe recibir una lista de enteros 
y retornar solo aquellos que sean primos.*

Honestamente, en este caso me salió un algoritmo bastante ineficiente, ya que este algoritmo inició como una busqueda de realizar un cribado de eratóstenes, pero en el camino salío un error conveniente, el cual al crear una lista se creaban mútliples copias de todos los números de la lista original que no fueran primos, pero se creaba una única copia de cada número primo que había en la lista original; entonces en la nueva lista solo era necesario depurar los números no primos mediante borrar todos los números cuyo conteo en esta lista fuera distinto de 1. Este algoritmo es muy ineficiente y solo puede entregar los números primos de 1 hasta el orden de 10^4 en menos de 10 minutos.

```python
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
```
## Punto 4

*Escribir una función que reciba una lista de números enteros y 
retorne la mayor suma entre dos elementos consecutivos*

Este punto no tiene mucho misterio, se utiliza un bucle **for** que recorre la lista y cada item lo suma con su consecutivo, posteriormente cada suma se agrega a una lista; se ordena esta lista con **.sort()** y se imprime el último ítem de esta lista.
```python

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
```
(aclaración: se importó random para probar el algoritmo empleando una lista aleatoria)

## Punto 5
*Escribir una función que reciba una lista de string y 
retorne unicamente aquellos elementos que tengan los mismos caracteres. 
e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]*

Este punto emplea un bucle **for** para recorrer la lista de palabras dada y a cada palabra le aplica la función **sorted()** y crea una lista con las listas de los carácteres de estas palabras ordenadas. Luego cuenta cuantas listas de estas son iguales y luego entrega una nueva lista con las palabras de la lista original cuyo indice sea el mismo que la lista creada con **sorted()** que tiene múltiples apariciones.

```python
palabras = ["amor", "roma", "perro", "mora", "ramo", "gatito", "toga", "ratón", "tórax", "maro"]
def buscador(palabras:list):
    lista_nuevas_p = []
    resultado_casi = []
    resultado = []
    for p in palabras:
        nueva_p = sorted(p)
        lista_nuevas_p.append(nueva_p)
    #print(lista_nuevas_p)
    for pp in range(0,len(lista_nuevas_p),1):
        #print(lista_nuevas_p.count(lista_nuevas_p[pp]))
        if lista_nuevas_p.count(lista_nuevas_p[pp]) > 1  and not palabras[pp] in resultado:
            resultado_casi.append(palabras[pp])
    for ppp in range(0,len(resultado_casi),1):
        if not sorted(resultado_casi[ppp]) == sorted(resultado_casi[ppp - 1]):
            pedazo_resultado = []
            for ppp in range(0,len(resultado_casi),1):
                if not sorted(resultado_casi[ppp]) == sorted(resultado_casi[ppp - 1]):
                    pedazo_resultado.append(resultado_casi[ppp])
    return resultado_casi

if __name__ == "__main__":
    print(" esta es tu lista original: ")
    print(palabras)
    print(" esta es tu lista con las palabras que repiten todos sus caracteres")
    p1 = buscador(palabras)
    print(p1)
```