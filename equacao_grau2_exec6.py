
import math
a = float(input('Entre com o calor de A: '))
delta = 0

def delta(a, b, c):
    return math.pow(b,2) - 4 * a * c

if a == 0:
    print('Não é uma equação do segundo grau :')
    print('Fim')
else:
    b = float(input('Entre com o calor de B: '))
    c = float(input('Entre com o calor de C: '))
    delta = delta(a, b, c)

if delta == 0:
    print('A equação possui apenas uma equação real:')
elif delta != 0:
    print('A equação possui duas reaizes reais.')