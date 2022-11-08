
def Metodo(lista, largo_lista):
    
    salto =  int(largo_lista / 2)

    while (salto > 0):
        
        for I in range(salto , (largo_lista)):
            auxiliar = lista[I]
            J = I - salto
            while ((J > -1) & (lista[J] > auxiliar)):
                lista[J + salto] = lista[J]
                J = J - salto
            lista[J + salto] = auxiliar

        salto = int(salto / 2)
    
    return lista
