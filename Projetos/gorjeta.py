# João trabalha como garçom em um restaurante e precisa calcular a gorjeta 
# que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta
# de 10%, mas alguns clientes podem escolher dar mais ou menos.

# Para agilizar o processo, João quer um programa que receba o valor total 
# da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. 
# O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

def calcular_gorjeta(porcentagem_gorjeta, valor_conta):
    return porcentagem_gorjeta + valor_conta


gorjeta = int(input('Digite o valor da gorjeta: '))
valor = int(input('Digite o valor da conta: '))

print(f'O valor da conta ficou: {calcular_gorjeta(gorjeta, valor)}')