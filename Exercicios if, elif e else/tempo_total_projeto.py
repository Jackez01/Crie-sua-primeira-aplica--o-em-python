#Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. 
# No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

#Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
# Se algum valor for negativo, mostre uma mensagem informando o erro.

numero1 = int(input('Informe os dias para atividade: '))
numero2 = int(input('Informe os dias para atividade: '))
numero3 = int(input('Informe os dias para atividade: '))

tempo_total = numero1+numero2+numero3

if numero1<0 or numero2<0 or numero3<0:
    print('Erro: Digite valores maiores que 0.')
else:
    print(f'O valor total de dias é de {tempo_total}')