#importante a os para limpar o terminal quando a finção finalizar_app for ativada
import os

restaurantes = ['pizza', 'lanche']


def exibir_nome_programa():

    print('''  
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      ''')

def exibir_opcoes():

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    #no windows
    print('Finalizando App\n')

#função que volta a tela de inicio para todas as outras funções
def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu inicial ')
    main()


def opcao_invalida():
    print('opcão inválida\n')
    voltar_menu_principal()
    #chama main para limpar tudo
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes \n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_menu_principal()

def lista_restaurante():
    exibir_subtitulo('Os restaurantes cadastrados são: \n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    
    voltar_menu_principal()

def escolher_opcao():

    try:
        #O input sempre recebe uma string, precisa fazer a formatação para int
        opcao_escolhida = int(input('escolha um valor:'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
           lista_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida() 
    except:
        print('Opção inválida')

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


#opcao_escolhida = int(input('Escolha uma opção: '))
#match opcao_escolhida:
    #case 1:
    #    print('Adicionar restaurante')
    #case 2:
    #    print('Listar restaurantes')
    #case 3:
    #    print('Ativar restaurante')
    #case 4:
    #    print('Finalizar app')
    #case _:
    #    print('Opção inválida!')