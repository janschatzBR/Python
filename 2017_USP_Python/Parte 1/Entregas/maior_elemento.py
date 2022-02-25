def maior_elemento(lista):

    #lista.sort()

    #x = int(len(lista))
   
    #print(lista[x])
    #return lista[x]

    print(max(lista))
    return max(lista)

n = 1
lista = []

while n >= 0:
    n = int(input("digite número inteiro: "))
    lista.append(n)    

maior_elemento(lista)
