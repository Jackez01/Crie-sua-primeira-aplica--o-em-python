#Utilizando o dicionário criado no item 1:

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

pessoa = {'nome':'Lucas', 'idade':19, 'cidade':'Paulínia'}

#adiciona um campo
pessoa['profissão'] = 'Analista' 

#Atualiza um campo
pessoa['idade'] = 20

#Deleta um campo
del pessoa['cidade']

print(pessoa)