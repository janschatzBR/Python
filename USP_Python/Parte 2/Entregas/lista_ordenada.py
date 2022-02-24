def ordenada(lista):
    for i in range(len(lista)-1):
        if (lista[i]) <= (lista[i+1]):
            i =+ 1
        else:
            return False
    return True
