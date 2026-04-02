
import os
import sys
tarefas = []

def voltar_inicio():
    input('Digite qualquer tecla para voltar ao inicio.')
    main()

def cadastrar_tarefa():
    cadastrar = input('Digite a tarefa que você quer adicionar: ')
    tarefas.append(cadastrar)
    print('A tarefa foi cadastrada com sucesso!')
    voltar_inicio()

def visualizar_tarefas():
    if tarefas:
        for i, tarefa in enumerate(tarefas, 1):
            print(f'{i}. {tarefa}')
    else:
        print('Nenhuma tarefa cadastrada.')
    voltar_inicio()

def remover_tarefa():
    tarefa_escolhida = input('Digite a tarefa que você quer remover: ')
    if tarefa_escolhida in tarefas:
        tarefas.remove(tarefa_escolhida)
        print('Tarefa removida com sucesso!')
    else:
        print('Tarefa inválida!')

    
    voltar_inicio()


def finalizar():
    print('Finalizando o aplicativo')
    sys.exit()


def opcoes():
    try:
        escolha_usuario = int(input( 
        '1.Adicionar tarefa\n'
        '2. Visualizar tarefa\n' 
        '3. Remover tarefa\n' 
        '4. Sair\n'
        'Escolha uma das opções: \n'))
    except ValueError:
        print('Digite um número válido')
        voltar_inicio()
        return
    
    if escolha_usuario == 1:
        cadastrar_tarefa()

    elif escolha_usuario == 2:
        visualizar_tarefas()
    elif escolha_usuario == 3:
        remover_tarefa()
    elif escolha_usuario == 4:
        finalizar()

    #limpa o terminal de acordo com o sistema operacional    
def main():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
        
    opcoes()


# faz o programa rodar quando é executado diretamente
if __name__ == '__main__':
    main()

