
def Metodo1(lista, largo_lista):
    # Metodo de Inserción Directa

    for I in range(1, largo_lista):
        
        auxiliar = lista[I]
        k = I - 1
        sw = False

        while (( not sw ) & (k >= 0)):

            if (auxiliar < lista[k]):
                lista[k + 1] = lista[k]
                k = k - 1
            else:
                sw = True
                
        lista[k + 1] = auxiliar 

    return lista


def Metodo2(lista, largo_lista):
    # Metodo de Inserción Binaría

    for I in range(1, largo_lista):
        
        auxiliar = lista[I]
        primero = 0
        ultimo = I - 1

        while (primero <= ultimo):
            centro = int((primero + ultimo) / 2)
            if (auxiliar < lista[centro]):
                ultimo = centro - 1
            else:
                primero = centro + 1

        for k in range(I - 1, (primero - 1), -1):
            lista[k + 1] = lista[k]

        lista[primero] = auxiliar
    
    return lista
