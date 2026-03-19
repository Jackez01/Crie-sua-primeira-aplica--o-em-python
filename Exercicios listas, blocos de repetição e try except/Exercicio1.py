#Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

from datetime import date

ano_atual = date.today().year

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Lucas', 'Bianca', 'Marcelo', 'Nicolle']
ano = [2001, ano_atual]

print(numeros)
print(nomes)
print(ano)