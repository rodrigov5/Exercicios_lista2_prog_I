dia = int(input('Entre com o Dia: '))
mes = int(input('Entre com o Mês: '))
ano = int(input('Entre com o Ano: '))

if dia < 30 and mes < 12 and ano < 3000:
    print(f'{dia}/{mes}/{ano}')
    print('Data válida!')
else:
    print('Data inválida!')