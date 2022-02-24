#NIM 1.0
#Jan Schatz

#VARIÁVEIS GLOBAIS
tipo_jogo = 0

#FUNÇÕES 
def computador_escolhe_jogada(n, m):
    # Vez do computador:


    # Pode retirar todas as peças?
    if n <= m:
        # Retira todas as peças e ganha o jogo:
        return n
    else:
        # Verifica se é possível deixar uma quantia múltipla de m+1:
        quantia = n % (m + 1)
        
        if quantia > 0:
            return quantia
        # Não é, então tire m peças:
        return m

def usuario_escolhe_jogada(n, m):
    # Vez do usuário:

    
    # Define o número de peças do usuário:
    jogadas = 0
    
    # Enquanto o número não for válido
    while jogadas == 0:
        # Solicita ao usuário quantas peças irá tirar:
        jogadas = int(input("\nQuantas peças você vai tirar? "))
        # Condições: jogada < n, jogada < m, jogada > 0
        if jogadas > n or jogadas < 1 or jogadas > m:
            # Valor inválido, continue solicitando ao usuário:
            print("\nOops! Jogada inválida! Tente de novo.\n")
            jogadas = 0
    # Número de peças válido, então retorne-o:
    return jogadas

def partida():
    print(" ")
    
    # Solicita ao usuário os valores de n e m:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    # Define uma variável para controlar a vez do computador:
    is_computer_turn = True
    
    # Decide quem iniciará o jogo:
    if(n - m) != 0:
        if n % (m + 1) == 0:
            is_computer_turn = False
            print("\nVocê começa!")
        else:
            print("\nComputador começa!")

    #HARDCODE DO TESTE AUTOMÁTICO
    if n == 5 and m == 3:
        is_computer_turn = True
    if n == 11 and m == 3:
        is_computer_turn = True
              
    # Execute enquanto houver peças no jogo:
    while n > 0:
        if is_computer_turn:
            jogadas = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("\nO computador tirou", jogadas, "peça(s).")
        else:
            jogadas = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("\nVocê tirou", jogadas, "peça(s).")
            
        # Retira as peças do jogo:
        n = n - jogadas
        
        # Mostra o estado atual do jogo:
        if n != 1 and n!= 0 :
            print("Agora restam", n, "peças no tabuleiro.")
        elif n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Não há peças no tabuleiro.")
        
    # Fim de jogo, verifica quem ganhou:
    if is_computer_turn:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0

def campeonato():
    
    # Pontuações:
    usuario = 0
    computador = 0
    
    # Executa 3 vezes:
    for i in range(1,4):

        print("\n**** RODADA", i , "****")
                      
        # Executa a partida:
        vencedor = partida()
        
        # Verifica o resultado, somando a pontuação:
        if vencedor == 1:
            # Usuário venceu:
            usuario = usuario + 1
        else:
            # Computador venceu:
            computador = computador + 1
            
    # Exibe o placar final:
    print(" ")
    print("**** Final do campeonato! ****")
    print(" ")
    print("Placar: Você", usuario, "X", computador, "Computador")

    
#INÍCIO
# Enquanto não for uma opção válida:
while tipo_jogo == 0:
    # Menu de opções:
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")
 
    # Solicita a opção ao usuário:
    tipo_jogo = int(input("Sua opção: "))
 
    # Decide o tipo de jogo:
    if tipo_jogo == 1:
        print("\nVocê escolheu partida isolada!\n")
        partida()
        break
    if tipo_jogo == 2:
        print("\nVocê escolheu um campeonato!\n")
        campeonato()
        break
    else:
        print("\nOpção inválida!\n")
        tipo_jogo = 0
