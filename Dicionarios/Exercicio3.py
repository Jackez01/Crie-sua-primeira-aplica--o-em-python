#Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

numeros = {}

for i in range(1, 6):
    numeros[i] = i**2

print(numeros)