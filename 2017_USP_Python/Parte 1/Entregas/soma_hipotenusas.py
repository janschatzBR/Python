# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
#soma_hipotenusas(25)
# deve devolver 105

def calcular_hipotenusa(a, b):
    return ((a*a) + (b*b))
 
def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        c_aux = (c*c)      
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (c_aux == calcular_hipotenusa(a, b)):
                    #print(a, " - " ,b , " - " , c)
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1

    print(soma)
    return soma

n = int(input("Número: "))
soma_hipotenusas(n)
