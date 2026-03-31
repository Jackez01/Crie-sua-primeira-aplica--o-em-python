# Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. 
# Ela quer um programa onde o computador escolhe um número aleatório 
# entre 1 e 100, e o jogador tem que adivinhar qual é.

# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, 
# impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e
# permita que o usuário tente adivinhar o número. O programa deve informar se 
# o palpite é maior ou menor que o número correto, até que o usuário acerte. 
# Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .
import random

def jogo():
    #escolhe um número aleatório entre 1 e 100
    numero = random.randint(1, 100)
  
    while True:
        try:         
            escolha_jogador = int(input('Escolha um número entre 1 e 100: '))

            if not 0 <= escolha_jogador <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
            if escolha_jogador > numero:
                print('Escolha muito alta, tente novamente')
            elif escolha_jogador < numero:
                print('Escolha muito baixa, tente novamente!')
            else:
                 print(f'Parabéns você acertou o número: {numero}')
                 break

        except ValueError as e:
            print(f'Entrada invalida {e}')
jogo()

