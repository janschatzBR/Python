def retangulo(x,y):
    cont = 1
    while cont <= y:
        i = 1
        while i <= x:
            print('#', end = "")
            i = i + 1
        print()
        cont = cont + 1

x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

retangulo(x,y)
