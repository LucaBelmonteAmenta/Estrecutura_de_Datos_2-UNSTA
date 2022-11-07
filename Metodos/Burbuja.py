def Intercambiar(lista, indice1, indice2):
    lista[indice1], lista[indice2] = lista[indice2], lista[indice1]
    return lista


def Metodo1(lista, largo_lista):
    
    for I in range(largo_lista - 1):
        for J in range(largo_lista - 1):
            if(lista[J] > lista[J + 1]):
                auxiliar = lista[J]
                lista[J] = lista[J + 1]
                lista[J + 1] = auxiliar

    return lista


def Metodo2(lista, largo_lista):
    
    for I in range(largo_lista - 1):
        for J in range(largo_lista - (I + 1)):
            if(lista[J] > lista[J + 1]):
                auxiliar = lista[J]
                lista[J] = lista[J + 1]
                lista[J + 1] = auxiliar
    return lista


def Metodo3(lista, largo_lista):

    bandera = False
    while (bandera == False):
        bandera = True
        for k in range(largo_lista - 1):
                if (lista[k] > lista[k + 1]):
                    lista = Intercambiar(lista, k, k + 1) # llamada a un procedimiento de intercambio
                    bandera = False

    return lista
