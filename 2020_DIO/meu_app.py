print("Meu primeiro programa em Python")

z = 7
print("z é igual a " + str(z))
print(type(z))

a = int(input('Entre com o valor de a: '))
b = int(input('Entre com o valor de b: '))

print("a / b = " + str(a / b))
print("a / b = {} ".format(a / b))  #não importa o tipo

resultado = a / b
print(resultado)

if a > b:
    print("a é maior que b")
elif a < b:
    print("a é menor que b")
else:
    print("a é igual a b")