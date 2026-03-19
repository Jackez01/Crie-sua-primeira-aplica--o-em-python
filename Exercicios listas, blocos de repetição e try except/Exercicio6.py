#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

numeros = [1, 2, 3, 'Lucas', 5, 6, 7, 8, 9, 10]
soma = 0

try:
    for numero in numeros:
        soma += numero
    print(f'A soma dos números é {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

