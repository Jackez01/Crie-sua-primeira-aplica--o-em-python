#Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado.
#  Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
# Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
# Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

maca = int(input('Digite a quantidade de maçãs vendidas: '))
banana = int(input('Digite a quantidade de banana vendidas: '))

if banana>maca:
    print('Você vendeu mais maçãs esse mês')
elif maca<banana:
    print('Você vendeu mais bananas esse mês')
else:
    print('A quantidade de vendas foi igual')