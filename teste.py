import random

def jogo():
    numero = random.randint(1, 100)
    escolha_jogador = int(input('Escolha um número entre 1 e 100: '))
  
    while escolha_jogador != numero:
          try:
            
            if not 0 < escolha_jogador < 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
            if escolha_jogador > numero:
                print('Escolha muito alta, tente novamente')
            elif escolha_jogador < numero:
                print('Escolha muito baixa, tente novamente!')

            escolha_jogador = int(input('Escolha um número entre 1 e 100: '))

          except ValueError as e:
              print(f'Entrada invalida {e}')
    print(f'Parabéns você acerrtou o número: {numero}')
jogo()