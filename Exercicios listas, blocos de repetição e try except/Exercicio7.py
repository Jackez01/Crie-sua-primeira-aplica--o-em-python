#Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

try:
    for numero in numeros:
        soma += numero
        
    media = soma /len(numeros)
    print(f'A media dos valores da lista é {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média')
except Exception as e:
    print(f'Ocorreu um erro: {e}')