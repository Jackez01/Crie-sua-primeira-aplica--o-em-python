import random

def jogo():
    numero = random.randint(1, 100)
    escolha_jogador = int(input('Escolha um número entre 1 e 100: '))

    while escolha_jogador != numero:
        if escolha_jogador > numero:
            print('Escolha muito alta, tente novamente')

        elif escolha_jogador < numero:
            print('Escolha muito baixa, tente novamente!')
        
        escolha_jogador = int(input('Escolha um número entre 1 e 100: '))
    print(f'Parabéns, você acertou número: {numero}')

jogo()