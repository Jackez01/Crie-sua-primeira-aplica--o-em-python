# Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. 
# Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

# Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

def soma(x):
    #return x * (x + 1) // 2 --> poderia fazer assim que o código ficaria mais limpo
    
    i = 0
    somatoria = 0
    
    while i< x:
        
        i += 1
        somatoria +=i
    return somatoria



numero = int(input('Digite um número: '))
print(f'A somatoria é {soma(numero)}')