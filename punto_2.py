"""Realice una función que permita validar si una palabra es un palíndromo. 
Condición: No se vale hacer slicing para invertir la palabra y verificar 
que sea igual a la original."""
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