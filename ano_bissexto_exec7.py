ano = int(input('Entre com um valor correspondente a um determinado ano: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('É bissexto!')
else:
    print('Não é bissexto!')
