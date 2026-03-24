numero1 = int(input('Informe os dias para atividade: '))
numero2 = int(input('Informe os dias para atividade: '))
numero3 = int(input('Informe os dias para atividade: '))

tempo_total = numero1+numero2+numero3

if numero1<0 or numero2<0 or numero3<0:
    print('Erro: Digite valores maiores que 0.')
else:
    print(f'O valor total de dias é de {tempo_total}')