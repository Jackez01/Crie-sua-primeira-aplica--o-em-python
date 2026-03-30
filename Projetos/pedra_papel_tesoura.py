# Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. 
# Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. 
# O computador escolherá aleatoriamente uma opção. 
# O programa deve exibir quem venceu a partida. Lembrando que:

# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate.

import random

def pedra_papel_tesoura():
    #lista das opções criadas
    lista = ['pedra', 'papel', 'tesoura']
    #fazendo com que o computador escolha uma opcao aleatoria da lista
    escolha_computador = random.choice(lista)
    escolha_jogador = input('Escolha entre pedra, papel e tesoura: ').lower()
    
    #se a escolha do jogador não estiver na lista...
    if escolha_jogador not in lista:
        print('Escolha inválida!')
        #O return encerra a execução da função imediatamente Ele faz o Python sair da função
        return
    
    print(f'A escolha do computador foi: {escolha_computador}')

    if escolha_jogador == escolha_computador:
        print('Empate!')
    
    elif (
        (escolha_computador == 'tesoura' and escolha_jogador =='pedra') or
        (escolha_computador == 'papel' and escolha_jogador =='tesoura') or
        (escolha_computador == 'pedra' and escolha_jogador == 'papel')
    ):
        print('Você venceu!')
    else:
        print('Você perdeu!') 
    
pedra_papel_tesoura()



