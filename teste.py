while True:

    login = input('Digite um nome de usuário: ')
    password = input('Digite uma senha: ')

    if len(login) < 5:
        print('Digite um login com pelo menos 5 caracteres')
        continue
    
    if len(password) < 8:
        print('Digite uma senha com pelo menos 8 caracteres')
        continue
    
    print('Cadastro realizado com sucesso!')
    break