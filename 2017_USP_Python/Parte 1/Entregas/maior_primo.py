def maior_primo(n):

    cont = 2
    ehNroPrimo = True
 
    while (cont < n and ehNroPrimo):
        ehNroPrimo = not ((n % cont) == 0)
        cont += 1
  
    if (ehNroPrimo):
        return n
    else:
    
        primos = []
        for i in range(n):
            c = 0
            for j in range(n):
                if i%(j+1) == 0: 
                    c += 1
            if c == 2:
                primos.append(i)

        return(max(primos))
