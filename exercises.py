lista = ["cachorro", "gato", "elefante"]
print(lista)

print("\nmax")
print(max(lista))

print("\nappend lobo")
lista.append("lobo")
print(lista)

print("\nappend X")
lista.append(input("Insira novo animal para a lista: "))
print(lista)

print("\nsort")
lista.sort()
print(lista)

print("\npop")
lista.pop()
print(lista)

print("\npop [2]")
lista.pop(2)
print(lista)

print("\nremove cachorro")
lista.remove("cachorro")
print(lista)

print("\nreverse")
lista.reverse()
print(lista)

print(len(lista))

print("\ntuple")
tupla1 = ("zebra", "rato", "arara")  #tupla não permite mutações
print(tupla1)

print("\nlista convertida em tupla")
tupla2 = tuple(lista)
print(type(tupla1))
print(tupla2)

print("\ntupla convertida em lista")
lista = list(tupla1)
print(lista)

print("\nlambda para contar letras")
contador_letras = lambda lista: [len(x) for x in lista] #lamba cria uma função anônima substituindo a criação de métodos (def)
print(contador_letras(lista))

print("\ndicionario")
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
    'resto': lambda a, b: a % b
}
print(type(calculadora))
soma = calculadora['soma']
print(soma(10, 5))