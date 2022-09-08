a = float(input('Entre com a medida do lado do triangulo: '))
b = float(input('Entre com a medida do lado do triangulo: '))
c = float(input('Entre com a medida do lado do triangulo: '))

if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
elif (a == b) and (a == c) :
        print('Equilatero')
elif (a==b) or (a==c) or (b==c):
        print('Isósceles')
else:
        print('Escaleno')