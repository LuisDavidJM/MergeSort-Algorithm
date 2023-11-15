#Se encarga de dividir el array en 2
def merge_sort(lista):
    #Array ya ordenado
   if len(lista) < 2:
      return lista
    
    #Divide el array en 2
   else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])

        return merge(right, left)

#Se encarga de intercalar los elemanetos de las dos divisiones
def merge(lista1, lista2):
    i, j = 0, 0
    result = []
 
   # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
 
   # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
 
    return result

#lista = [31,3,88,1,4,2,42]
lista = [1, 34, 78, 12, 56, 89, 23, 45, 67, 90, 2, 55, 31, 65, 96, 43, 87, 32, 66, 97, 98, 44, 88, 33, 67]
print("Original: ", lista)
print("Ordenado: ", merge_sort(lista))