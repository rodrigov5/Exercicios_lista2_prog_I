numero = int(input('Entre com um numero ate 1000: '))

def achaUnidade(num):
    return numero % 10

unidade = achaUnidade(numero)

def achaDezena(num):
    numero = num
    numero = (numero - unidade) / 10
    dezena = numero % 10
    return int(dezena)

dezena = achaDezena(numero)

def achaCentena(num):
    numero = num
    numero = (numero - unidade) / 10
    numero = (numero - dezena) / 10
    centena = numero
    return int(centena)

centena = achaCentena(numero)

