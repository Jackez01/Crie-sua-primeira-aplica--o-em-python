#Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.


frase = "o gato preto pulou no muro e o gato caiu"

# separa a frase em palavras
palavras = frase.split()

frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)