#NIM 1.0
#Jan Schatz

def computador_escolhe_jogada(n, m):
    global ganhador
    ganhador = 0
    if n > 0:
        if (n - m) != 0:
            if (n - m) < 0:
                if n == 1:
                    print('O computador tirou uma peça.\nFim de jogo. O computador ganhou!\n')
                    n -= n
                    ganhador += 2
                else:
                    print('O computador tirou', n, 'peças.\nFim de jogo. O computador ganhou!\n')
                    n -= n
                    ganhador += 2
            else:
                if (m + 1) % (n - m) == 0 or (m + 1) % (n - m) == (m + 1):
                    n -= m
                    if m == 1 and n == 1:
                        print('O computador tirou uma peça\nSobrou uma peça no tabuleiro.')
                        if n != 0:
                            usuario_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
                            ganhador += 2
                    elif m == 1 and n != 1:
                        print('O computador tirou uma peça\nRestam', n, 'peças no tabuleiro.')
                        if n != 0:
                            usuario_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
                            ganhador += 2
                    elif m != 1 and n == 1:
                        print('O computador tirou', m, 'peças\nSobrou uma peça no tabuleiro.')
                        if n != 0:
                            usuario_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
                            ganhador += 2
                    elif m != 1 and n != 1:
                        print('O computador tirou', m, 'peças\nRestam', n, 'peças no tabuleiro.')
                        if n != 0:
                            usuario_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
                            ganhador += 2
                else:
                    var = m - 1
                    n -= var
                    if m == 1 and n == 1:
                        print('O computador tirou uma peça\nSobrou uma peça no tabuleiro.')
                        if n != 0:
                            usuario_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
                            ganhador += 2
                    elif m == 1 and n != 1:
                        print('O computador tirou uma peça\nRestam', n, 'peças no tabuleiro.')
                        if n != 0:
                            usuario_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
                            ganhador += 2
                    elif m != 1 and n == 1:
                        print('O computador tirou', var, 'peças\nSobrou uma peça no tabuleiro.')
                        if n != 0:
                            usuario_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
                            ganhador += 2
                    elif m != 1 and n != 1:
                        print('O computador tirou', var, 'peças\nRestam', n, 'peças no tabuleiro.')
                        if n != 0:
                            usuario_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
                            ganhador += 2
        else:
            n -= m
            print('O computador tirou', m, 'peças.')
            print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
            ganhador += 2
    else:
        print('Não há mais peças no tabuleiro.\nFim de jogo. O computador ganhou!\n')
        ganhador += 2

def usuario_escolhe_jogada(n, m):
    global ganhador
    ganhador = 0
    if n > 0:
        choice = int(input('Quantas peças você vai tirar?\n'))
        if choice <= m and choice > 0:
            if (n - choice) < 0:
                while (n - choice) < 0 or choice < 0:
                    print('Jogada inválida, tente novamente.')
                    choice = int(input('Quantas peças voce vai tirar?\n'))
                    if (n - choice) == 0 and choice > 0:
                        if choice == 1:
                            print('Você tirou uma peça')
                            print('Não há mais peças no tabuleiro.\nFim de jogo. você ganhou!')
                            ganhador += 1
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                            ganhador += 1
            else:
                n -= choice
                if n == 0:
                    print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                    ganhador += 1
                else:
                    if choice == 1 and n == 1:
                        print('Você tirou uma peça\nSobrou uma peça no tabuleiro')
                        if n != 0:
                            computador_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                            ganhador += 1
                    elif choice == 1 and n != 1:
                        print('Voce tirou uma peça\nRestam', n, 'peças no tabuleiro.')
                        if n != 0:
                            computador_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                            ganhador += 1
                    elif choice != 1 and n == 1:
                        print('Você tirou', choice, 'peças\nSobrou uma peça no tabuleiro.')
                        if n != 0:
                            computador_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                            ganhador += 1
                    elif choice != 1 and n != 1:
                        print('Você tirou', choice, 'peças\nRestam', n, 'peças no tabuleiro.')
                        if n != 0:
                            computador_escolhe_jogada(n, m)
                        else:
                            print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                            ganhador += 1
        else:
            while choice > m or choice <= 0 or (n - choice) < 0:
                print('Jogada inválida, tente novamente.')
                choice = int(input('Quantas peças você vai tirar ?\n'))
            n -= choice
            if choice == 1 and n == 1:
                print('Você tirou uma peça\nSobrou uma peça no tabuleiro')
                if n != 0:
                    computador_escolhe_jogada(n, m)
                else:
                    print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                    ganhador += 1
            elif choice == 1 and n != 1:
                print('Você tirou uma peça\nRestam', n, 'peças no tabuleiro.')
                if n != 0:
                    computador_escolhe_jogada(n, m)
                else:
                    print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                    ganhador += 1
            elif choice != 1 and n == 1:
                print('Você tirou', choice, 'peças\nSobrou uma peça no tabuleiro.')
                if n != 0:
                    computador_escolhe_jogada(n, m)
                else:
                    print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                    ganhador += 1
            elif choice != 1 and n != 1:
                print('Você tirou', choice, 'peças\nRestam', n, 'peças no tabuleiro.')
                if n != 0:
                    computador_escolhe_jogada(n, m)
                else:
                    print('Não ha mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
                    ganhador += 1
    else:
        print('Não há mais peças no tabuleiro.\nFim de jogo. Você ganhou!\n')
        ganhador += 1
 
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    try:
        if (m + 1) % (n - m) == 0 or (m + 1) % (n - m) == (m + 1):
            print('O computador começa!')
            computador_escolhe_jogada(n, m)
        else:
            print('Você começa!')
            usuario_escolhe_jogada(n, m)
    except ZeroDivisionError:
        print('O computador começa!')
        computador_escolhe_jogada(n, m)
 
def campeonato():
    jogador = 0
    computador = 0
    i = 3
    for match in range(i):
        if match == 0:
            print('Voce escolheu um campeonato!')
            print('*** RODADA 1 ****')
            n = int(input('Quantas peças? '))
            m = int(input('Limite de peças por jogada? '))
            if (m + 1) % (n - m) == 0 or (m + 1) % (n - m) == (m + 1):
                print('Computador começa!')
                computador_escolhe_jogada(n, m)
                if ganhador == 1:
                    jogador += 1
                elif ganhador == 2:
                    computador += 1
            else:
                print('Você começa!')
                usuario_escolhe_jogada(n, m)
                if ganhador == 1:
                    jogador += 1
                elif ganhador == 2:
                    computador += 1
        elif match == 1:
            print('**** RODADA 2 ****')
            n = int(input('Quantas peças? '))
            m = int(input('Limite de peças por jogada? '))
            if (m + 1) % (n - m) == 0 or (m + 1) % (n - m) == (m + 1):
                print('Computador começa!')
                computador_escolhe_jogada(n, m)
                if ganhador == 1:
                    jogador += 1
                elif ganhador == 2:
                    computador += 1
            else:
                print('Você começa!')
                usuario_escolhe_jogada(n, m)
                if ganhador == 1:
                    jogador += 1
                elif ganhador == 2:
                    computador += 1
        elif match == 2:
            print('**** RODADA 3 ****')
            n = int(input('Quantas peças? '))
            m = int(input('Limite de peças por jogada? '))
            if (m + 1) % (n - m) == 0 or (m + 1) % (n - m) == (m + 1):
                print('O computador começa!')
                computador_escolhe_jogada(n, m)
                if ganhador == 1:
                    jogador += 1
                elif ganhador == 2:
                    computador += 1
            else:
                print('Você começa!')
                usuario_escolhe_jogada(n, m)
                if ganhador == 1:
                    jogador += 1
                elif ganhador == 2:
                    computador += 1
 
    print('Placar: Você', jogador, 'X', computador, 'Computador ')
    if jogador > computador:
        print('Parabéns!! Você foi o grande campeão!')
    else:
        print('Fim do jogo! O computador ganhou!')

#main 
print('Bem Vindo ao jogo do NIM! Escolha:\n')
opcao = int(input('1 - Para jogar uma partida isolada\n2 - Para jogar um campeonato (melhor de 3)\n0 = SAIR\n'))
 
if opcao == 1 or opcao == 2 or opcao == 0:
    if opcao == 1:
        partida()
    elif opcao == 2:
        campeonato()
    else:
        quit()
else:
    while opcao != 1 and opcao != 2 and opcao != 0:
        print('Ops, resposta invalida. Tente novamente ou 0 (zero) para sair.')
        opcao = int(input('1 - Para jogar uma partida isolada\n2 - Para jogar um campeonato (melhor de 3)\n0 - SAIR\n'))
    if opcao == 1:
        partida()
    elif opcao == 2:
        campeonato()
    else:
        quit()
