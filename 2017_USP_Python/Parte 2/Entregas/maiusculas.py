def maiusculas(frase):

    novo = []

    for c in frase:
        if c >= 'A' and c <= 'Z':
            novo.append(c)

    novo = ''.join(novo)

    return novo

"""
nmin = nmai = 0

for c in frase:
    if c >= 'a' and c <= 'z':
        nmin += 1
    elif c >= 'A' and c <= 'Z':
        nmai += 1

print("Número de minúsculas: %d"%(nmin))
print("Número de maiúsculas: %d"%(nmai))
print("Total de caracteres no texto: %d"%(len(frase)))
"""
