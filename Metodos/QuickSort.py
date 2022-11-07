  
def Metodo(lista, high, low = 0):
    
    if low < high:
        
        pivot = lista[high]
        i = low - 1

        for j in range(low, high):
            if lista[j] <= pivot:
                i = i + 1
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
        auxiliar = lista[i + 1]
        lista[i + 1] = lista[high]
        lista[high] = auxiliar

        pi = i + 1
  
        # Recursive call on the left of pivot
        Metodo(lista, pi - 1, low)
  
        # Recursive call on the right of pivot
        Metodo(lista, high, pi + 1)
    
    return lista
