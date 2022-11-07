
def Metodo1(lista, largo_lista):
    
    for I in range(largo_lista - 1):
        auxiliar = lista[I]
        k = I
        for J in range(I + 1, largo_lista):
            if (lista[J] < auxiliar):
                auxiliar = lista[J]
                k = J
        lista[k] = lista[I]
        lista[I] = auxiliar

    return lista


def Metodo2(lista, largo_lista):
    
    largo_lista = largo_lista - 1
    I = 0
    while (I < largo_lista):
        auxiliar = lista[I]
        k = I
        J = I
        while (J < largo_lista):
            J = J + 1
            if (lista[J] < auxiliar):
                auxiliar = lista[J]
                k = J
        lista[k] = lista[I]
        lista[I]= auxiliar
        I = I + 1

    return lista
