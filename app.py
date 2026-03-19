#importante a os para limpar o terminal quando a finção finalizar_app for ativada
import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                 {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                 {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


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
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_menu_principal()

def lista_restaurante():
    exibir_subtitulo('Os restaurantes cadastrados são: \n')
    print(f'{'Nome do restaurante: '.ljust(20)} |  {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        #ljust serve para justificar determinado numero de caracteres
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado == True
            #troca o estado da variavel
            restaurante['ativo'] = not restaurante['ativo']
            mensagem  = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

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
            alternar_estado_restaurante()
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