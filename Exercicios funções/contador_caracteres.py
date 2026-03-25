# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def contador_caracteres(string):
    return len(string)

palavra = input('Digite a palavra desejada: ')
print(f'A palavra {palavra} tem {contador_caracteres(palavra)} caracteres')


