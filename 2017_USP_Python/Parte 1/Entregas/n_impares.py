n = int(input("Digite o valor de n: "))
resultado = 1

while n != 0:
    if resultado % 2 != 0:
        print(resultado)
        n = n - 1
    resultado = resultado + 1
    
