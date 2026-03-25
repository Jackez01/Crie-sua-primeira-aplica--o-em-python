
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