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

En este caso, dado que no se permite aplicar el slicing a las cadenas de entrada,