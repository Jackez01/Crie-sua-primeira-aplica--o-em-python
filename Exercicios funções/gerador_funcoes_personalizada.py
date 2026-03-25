# Miguel está desenvolvendo um sistema de cupons de desconto e 
# precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

# Diante deste problema, crie uma closure que gere uma função capaz de 
# calcular o preço final com um desconto fixo definido pelo usuário.

def porcentagem_desconto(porcentagem):
    def calcular_preco(valor):
        return valor*(porcentagem/100)
    return calcular_preco

desconto = int(input('Digite a porcentagem de desconto: '))
calcular_preco_final = porcentagem_desconto(desconto)

compra = float(input('Digite o valor da compra: '))

print(f'O preço final seria{calcular_preco_final(compra)}')