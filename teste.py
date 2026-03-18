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