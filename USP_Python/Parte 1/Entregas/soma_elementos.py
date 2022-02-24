def soma_elementos(lista):

    x = 0
    lista.sort()
    
    for i in lista:
        x = x + i
           
    print(x)
    return x

n = 1
lista = []

while n >= 0:
    n = int(input("digite número inteiro: "))
    lista.append(n)    

soma_elementos(lista)
