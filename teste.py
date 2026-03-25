def soma_valores(valores):
    soma = 0
    for valor in valores:
        soma += int(valor)
    return soma
        

valores = input("Digite os valores das vendas: ").split()

print(f"A soma dos valores são {soma_valores(valores)}")