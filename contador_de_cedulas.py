# Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro.
# O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas.
# As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

# Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas
# de cada tipo serão necessárias para entregar o valor.
# O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) 
# e tratar erros de entrada caso não seja digitado um valor numérico válido.

#cedulas=None parametro opcional
def saque(valor, cedulas=None):
    # faz com que seja padrão esse dicionario
    if cedulas is None:
        cedulas = [100, 50, 20, 10, 5, 2]
    if valor <= 0:
        raise ValueError('Digite um valor válido')
    if valor %2 != 0:
        raise ValueError('Digite um valor multiplo de 2.')
    
    resultado = {}

    for cedula in cedulas:
        #divisão inteira, verifica quantas notas cabem
        quantidade = valor // cedula
        if quantidade > 0:
            #adiciona ao dicionario 
            resultado[cedula] = quantidade
            #Atualiza o valor restante
            valor %= cedula
    return resultado

def exibir_resultado(resultado):
    print('Cédulas entregues: ')
    #retorna pares chave/valor
    for cedula, quantidade in resultado.items():
        print(f'{quantidade} cédulas de R$ {cedula}')

def main():
    try:
        valor = int(input('Digite o valor do saque: '))
        resultado = saque(valor)
        exibir_resultado(resultado)
    except ValueError as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()