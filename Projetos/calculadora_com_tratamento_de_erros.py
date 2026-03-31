# Carlos está criando uma calculadora simples, mas quer garantir que o programa não 
# quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.

# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão.
# Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

# Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
# Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

def calculadora(x, y):
    
        
        escolha = input ('Escolha entre: | + | x | - | / |')
        

        if escolha == '+':
            return x+y
        elif escolha == 'x':
            return x*y
        elif escolha == '-':
            return x-y
        elif escolha == '/':
            if y == 0:
                raise ZeroDivisionError
            return x/y
        else:
            print('Escolha inválida')
            
    
try:
    primeiro_numero = int(input('Digite um número: '))
    segundo_numero = int(input('Digite o segundo número: '))
    resultado = calculadora(primeiro_numero, segundo_numero)
    print(resultado)
    
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")

except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')
