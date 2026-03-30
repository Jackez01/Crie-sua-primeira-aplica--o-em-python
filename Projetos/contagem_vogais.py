# Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais
#  há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

#função para contar as vogais
def contador_vogais(palavras):
    #vogais que vão ser reconhecidas
    vogais = 'aeiou'
    #quantidade de vogais inicial
    quantidade = 0

    #percorre as palavras no texto
    for palavra in palavras.lower():
        #ai percorrendo, caso tenha vogais adciona a quantidade
        if palavra in vogais:
            quantidade += 1
    return quantidade

frase = input('Digite uma frase: ')
print(f'A frase contém {contador_vogais(frase)} vogais.')

