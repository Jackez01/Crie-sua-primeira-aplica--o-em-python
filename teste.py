def validador(cpf_digitado):
    if not cpf_digitado.isdigit() :
        return 'Erro: digite apenas números.'
    if len(cpf_digitado) != 11: 
        return 'Digite 11 números do cpf.'
    return 'CPF valido'

cpf = input(f'Digite seu CPF: ')
print({validador(cpf)})

# def calcular_gorjeta(porcentagem, valor):
#     gorjeta = (porcentagem/100) * valor
#     total = valor + gorjeta
#     return gorjeta, total

# gorjeta, total = calcular_gorjeta(gorjeta, valor)

# print(f'Gorjeta: R$ {gorjeta:.2f}')
# print(f'Total: R$ {total:.2f}')