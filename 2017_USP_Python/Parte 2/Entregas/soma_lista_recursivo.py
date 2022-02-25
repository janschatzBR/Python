'''
def soma_lista(lista):
    l = lista
    soma = 0
    for i in range(len(lista)):
        #soma = lista[i] + soma_lista(lista)
        soma += l[i]
        #print(soma)
    return soma
'''

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])


