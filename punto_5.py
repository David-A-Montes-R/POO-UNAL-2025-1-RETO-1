"""Escribir una función que reciba una lista de string y 
retorne unicamente aquellos elementos que tengan los mismos caracteres. 
e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]"""
#gracias copilot
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