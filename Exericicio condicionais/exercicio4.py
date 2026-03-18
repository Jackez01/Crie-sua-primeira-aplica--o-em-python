 #Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else 
 # para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero > 0 and segundo_numero > 0:
    print('O ponto de encontro está no primeiro quadrante')
elif primeiro_numero < 0 and segundo_numero > 0:
    print('O ponto de encontro está no segundo quadrante')
elif primeiro_numero > 0 and segundo_numero < 0:
    print('O ponto de encontro está no quarto quadrante')
else:
    print('O ponto está localizado no eixo ou na origem')
