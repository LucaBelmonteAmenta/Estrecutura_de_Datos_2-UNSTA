def Metodo(lista, largo_lista):
    
    if len(lista) > 1:
 
         # Finding the mid of the array
        mid = largo_lista//2
 
        # Dividing the array elements
        L = lista[:mid]
 
        # into 2 halves
        R = lista[mid:]
 
        # Sorting the first half
        Metodo(L,len(L))
 
        # Sorting the second half
        Metodo(R,len(R))
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

    return lista
 