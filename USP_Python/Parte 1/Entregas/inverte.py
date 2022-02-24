#def inverte(lista):

    #for i in lista[::-1]:
    #    print (i)

    ##lista.reverse()
    ##    for i in lista:
    ##        print (i)


#n = 1
#lista = []

#while n > 0:
#    n = int(input("Digite um número: "))
#    lista.append(n)    

#inverte(lista)


#--------------------------------------------------

# Lista de valores:
lista = []

# Executa até ocorrer `break`
while True:

    # Pede ao usuário um valor inteiro:
    n = int(input("Digite um número: "))    
    # Se for zero, pare o loop:
    if n == 0: break
    # Se não, adiciona o valor a lista:
    lista.append(n)

# Percorre toda a lista de trás para frente:
for i in reversed(lista):
  # Exibe o valor na tela:
  print(i)
