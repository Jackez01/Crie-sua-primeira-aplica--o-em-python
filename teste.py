def calcular_gorjeta(porcentagem_gorjeta, valor_conta):
    return (porcentagem_gorjeta/100) * valor_conta + valor_conta


gorjeta = float(input('Digite o valor da gorjeta: '))
valor = float(input('Digite o valor da conta: '))

print(f'O valor da conta ficou: {calcular_gorjeta(gorjeta, valor):.2f}')

# def calcular_gorjeta(porcentagem, valor):
#     gorjeta = (porcentagem/100) * valor
#     total = valor + gorjeta
#     return gorjeta, total

# gorjeta, total = calcular_gorjeta(gorjeta, valor)

# print(f'Gorjeta: R$ {gorjeta:.2f}')
# print(f'Total: R$ {total:.2f}')