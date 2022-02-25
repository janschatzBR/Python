def busca(lista, elemento):
    '''(list, float) -> bool'''
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False
