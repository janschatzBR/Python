# Busca (pesquisa) binária

import random

def busca(lista,elemento):
    primeiro = 0
    ultimo = len(lista)-1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        print(meio)
        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False

# busca binária iterativa
def busca_bin_int(lista, elemento):
	esquerda, direita, tentativa = 0, len(lista), 1
	while 1:
		meio = (esquerda + direita) // 2
		aux_num = lista[meio]
		if elemento == aux_num:
			return tentativa
		elif elemento > aux_num:
			esquerda = meio
		else:
			direita = meio
		tentativa += 1


# busca binária recursiva
def busca_bin_rec(vet, num, esq, dir, tentativa):
	meio = (esq + dir) // 2
	aux_num = vet[meio]
	if num == aux_num:
		return tentativa
	elif num > aux_num:
		return binary_search_rec(vet, num, meio, dir, tentativa + 1)
	return binary_search_rec(vet, num, esq, meio, tentativa + 1)

# teste...
def teste():
	vet = [i for i in range(1, 1000001)]
	num = random.choice(vet)
	print('Numero escolhido: %d' % num)
	print('Tentativa (iterativo): %d' % binary_search_ite(vet, num))
	print('Tentativa (recursivo): %d' % binary_search_rec(vet, num, 0, len(vet), 1))

'''teste()'''
