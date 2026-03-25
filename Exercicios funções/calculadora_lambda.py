# Joana está participando de um processo seletivo para uma vaga de desenvolvedora 
# e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

# Sua tarefa é criar um programa usando funções lambda que receba dois números
# e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente

def calculadora(x, y, escolha):
    
    if escolha == '+':
        add = lambda x, y: x+y
        return add(x,y)
    
    elif escolha == '-':
        sub = lambda x, y: x-y
        return sub(x,y)
    
    elif escolha == '*':
        vezes = lambda x, y: x*y
        return vezes(x,y)
    
    elif escolha == '/':
        div = lambda x, y: x/y
        return div(x,y)

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
escolha = input('Escolha a operação: | + | - | * | / |')
resultado = calculadora(numero1, numero2, escolha)
print(resultado)
