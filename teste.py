def validador(cpf_digitado):
    if cpf_digitado == int:
        print('CPF válido')
        return validador
    else: 
        print('CPF inválido')

cpf = int(input(f'Digite seu CPF: '))
print({validador(cpf)})

# def calcular_gorjeta(porcentagem, valor):
#     gorjeta = (porcentagem/100) * valor
#     total = valor + gorjeta
#     return gorjeta, total

# gorjeta, total = calcular_gorjeta(gorjeta, valor)

# print(f'Gorjeta: R$ {gorjeta:.2f}')
# print(f'Total: R$ {total:.2f}')