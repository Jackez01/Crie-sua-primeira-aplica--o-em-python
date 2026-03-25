# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento.
# Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

# Exemplo de entrada:

# Digite o ano de nascimento: 2005  

# Digite o ano atual: 2025 


def calcular_idade(data_nascimento, data_atual): 
    return data_atual - data_nascimento 

data_nascimento = int(input('Digite o ano que você nasceu: '))
data_atual = int(input('Digite o ano atual: '))
idade = calcular_idade(data_nascimento, data_atual)
print(idade)