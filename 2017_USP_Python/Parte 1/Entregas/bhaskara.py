import math

a = int(input("digite a: "))
b = int(input("digite b: "))
c = int(input("digite c: "))

delta = ((b**2)-4*a*c)
    
if(delta<0):
        print("esta equação não possui raízes reais")
elif(delta==0):
        print("a raiz desta equação é", (-b + math.sqrt(delta)) / (2*a))
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    if(x1>x2):
        aux = x1
        x1 = x2
        x2 = aux
    print("as raízes da equação são", x1 ,"e", x2)
