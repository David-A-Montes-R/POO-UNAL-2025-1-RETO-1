"""Crear una función que realice operaciones básicas 
(suma, resta, multiplicación, división) entre dos números, 
según la elección del usuario, la forma de entrada 
de la función será los dos operandos y el caracter usado para la operación. 
entrada: (1,2,"+"), salida (3). """
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