
import os
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
    print (f'Essas são suas tarefas:\n {tarefas}')
    voltar_inicio()

def remover_tarefa():
    tarefa_escolhida = input('Digite a tarefa que você quer remover: ')
    for tarefa in tarefas:
        if tarefa_escolhida == tarefa:
            tarefas.remove(tarefa_escolhida)
        else:
            print('Tarefa inválida!')

    print('Tarefa removida com sucesso!')
    voltar_inicio()


# def finalizar():




def opcoes():
    
    escolha_usuario = int(input( 
    '1.Adicionar tarefa\n'
    '2. Visualizar tarefa\n' 
    '3. Remover tarefa\n' 
    '4. Sair\n'
    'Escolha uma das opções: \n'))
    
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
    if os.system=='nt':
        os.system('cls')
    else:
        os.system('clear')
        
    opcoes()


# faz o programa rodar quando é executado diretamente
if __name__ == '__main__':
    main()

