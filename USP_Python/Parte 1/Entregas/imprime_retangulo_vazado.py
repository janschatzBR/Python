def retangulo(x,y):
    cont = 1
    while cont <= y:
        i = 1
        while i <= x:
            #primeira ou última linha
            if cont == 1 or cont == y:
                print('#', end = "")
                i = i + 1
            #borda
            elif i == 1 or i == x:
                print('#', end = "")
                i = i + 1
            #dentro
            else:
                print(' ', end = "")
                i = i + 1
        print()
        cont = cont + 1

x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

retangulo(x,y)
