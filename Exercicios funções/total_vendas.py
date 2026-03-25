# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia.
# As vendas são informadas em uma única linha separadas por espaços.

# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.


def soma_valores(valores):
    soma = 0
    for valor in valores:
        soma += int(valor)
    return soma
        

valores = input("Digite os valores das vendas: ").split()

print(f"A soma dos valores são {soma_valores(valores)}")


