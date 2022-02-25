def remove_repetidos(lista):
    aux = []

    for i in lista:
        if i not in aux:
            aux.append(i)

    aux.sort()
    
    print(aux)
    return aux

n = 1
lista = []

while n >= 0:
    n = int(input("digite número inteiro: "))
    lista.append(n)    

remove_repetidos(lista)
