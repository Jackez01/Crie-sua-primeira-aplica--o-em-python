#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar 
# se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
usuario = 'Lucas'
password = 'lucas0612'

nome_de_usuario = input('Digite um nome de usuário: ')
senha = input('Digite uma senha: ')

print('Tente fazer login...\n')

if nome_de_usuario == usuario and senha == password:
    print('Credencias corretas, você entrou...\n')
else:
    print('Credenciais incorretas, tente novamente...\n')
    