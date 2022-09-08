def calc_reajuste(value):
    aumento = 0
    percentual = 0
    final = 0


    if salario <= 280: 
        aumento = salario * 0.20;
        percentual = 20
    elif salario > 280 and salario <= 700: 
        aumento = salario * 0.15
        percentual = 15
    elif salario > 700 and salario <= 1500: 
        aumento = salario * 0.10
        percentual = 10
    elif salario > 1500: 
        aumento = salario * 0.05
        percentual = 5

    final = salario + aumento
    return print(f'Salario antes do reajuste: {salario}.\nPercentual de aumento aplicado: {percentual}%.\nValor do aumento: {aumento}.\nSalário após aumento: {final}')




try:
    salario = float(input('Entre com o valor do salario do colaborador: '));
except ValueError :
    print('Erro, Por favor entre apenas com numeros')
else:
    calc_reajuste(salario)