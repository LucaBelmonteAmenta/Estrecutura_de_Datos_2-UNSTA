import random

def CrearLista(numero_elementos, nulo, rango_valores = (0,100), numeros_repetidos = False , ordenado = False, ordenado_ascendentemente = False):
    
    lista = []

    if not nulo:
        for i in range(numero_elementos):
            limite_superior, limite_superior = rango_valores
            random.shuffle(lista)

    
    
    return lista