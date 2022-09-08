num1 = float(input('Entre com um numero: '))
num2 = float(input('Entre com outro numero: '))

op = input("Digite a operação que deseja realizar: [+, -, /, *]: ")

def verifica():
    if resultado % 1 == 0:
        print('Inteiro')
        if resultado % 2 == 0:
            print('Par')
            if resultado > 0:
                print('Positivo')
            else:
                print('Negativo')
        else:
            print('Ímpar')
    else:
        print('Decimal')


if op == '+':
    resultado = num1 + num2
    print('Resultado', resultado)
    verifica()
elif op == '-':
    resultado = num1 - num2
    print("Resultado: ", resultado)
    verifica()
elif op == '/':
    resultado = num1 / num2
    print("Resultado: ", resultado)
    verifica()
elif op == '*':
    resultado = num1 * num2
    print("Resultado: ", resultado)
    verifica()
else:
    print("Valor Invalido")

