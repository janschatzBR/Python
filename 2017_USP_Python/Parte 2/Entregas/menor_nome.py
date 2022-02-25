import unicodedata as ud

def menor_nome(nomes):
    # Tamanho da lista
    len_list = len(nomes)

    # Normalizando a lista (suprimindo acentos)
    list_str = [(ud.normalize('NFKD', s ).encode('ASCII','ignore').decode()).strip() for s in nomes]

    # Produz uma lista com os tamanhos de cada elemento
    lens = [len(s) for s in list_str]

    # Tamanho do menor (ou menores, quando empate) elemento
    min_len = min(lens)

    # Lista para guardar as strings cujos tamanhos sejam iguais ao minimo
    mins = []

    for i in range(len_list):
        # String normalizada
        s = list_str[i]
        if len(s) == min_len:
            mins.append(nomes[i].strip())

    menor = mins[0].lower().capitalize()

    #return mins.lower().capitalize()
    #print(menor)
    return menor
