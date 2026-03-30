# Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. 
# Ele quer um programa que crie senhas aleatórias com letras maiúsculas,
# minúsculas, números e caracteres especiais.

# Crie um programa que gere uma senha aleatória de 12 caracteres, 
# contendo pelo menos uma letra maiúscula, uma minúscula,
# um número e um caractere especial. Exiba a senha gerada.



import random

def gerar_senha():
    #todas as possibilidades possiveis
    maiuscula ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    especiais = '!@#$%&'

    #lista para armazenar a senha e as exeigencias da senha
    senha = [random.choice(maiuscula),
           random.choice(minusculas),
           random.choice(numeros),
           random.choice(especiais)]
    
    #variavavel para conter todos os elementos na senha
    todos_caracteres = maiuscula + minusculas + numeros + especiais
    ##randomiza as escolhas com mais 8 caracteres 
    senha.extend(random.choices(todos_caracteres, k = 8))
    #usa random shuffle para reorganizar a lista para que os fixos não sejam sempre os primeiros
    random.shuffle(senha)
    #transforma a llista em uma string
    return ''.join(senha)

print(gerar_senha())