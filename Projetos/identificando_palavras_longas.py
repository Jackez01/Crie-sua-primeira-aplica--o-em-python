# Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. 
# Textos mais fáceis de ler costumam ter palavras curtas, 
# então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. 
# Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.


def medicao(frase):
    #lista que vai adicionar as palavras
    lista = []
    #percorre as palavras na frase e corta elas com split
    for palavra in frase.split():
        #se o tamanho da palavra tiver mais que 10 letras então...
        if len(palavra) > 10:
            #adiciona a palavra a lista
            lista.append(palavra)
    #se a lista não estiver vazia então retorne a lista
    if lista:
        return lista
    else: 
        return 'Nenhuma palavra grande encontrada'
   
texto = input('Digite a frase que você quiser: ')
print(f'As palavras grandes encntradas foram: {medicao(texto)}')