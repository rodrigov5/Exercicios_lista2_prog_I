
def salarioBruto(precoHora, horasTrabalhadas):
    return preco_horas * horasTrabalhadas

def descSindicato(salario):
    return salario * 0.03

def descFgts(salario):
    return salario * 0.11

def descInss(salario):
    return salario * 0.10

def descIR(salario):
    descontoIR = 0
    if salario <= 900:
        descontoIR = 0
    elif salario > 900 and salario <= 1500:
        descontoIR = 0.05
    elif salario > 1500 and salario <= 2500:
        descontoIR = 0.10
    elif salario > 2500:
        descontoIR = 0.20

    return salario * descontoIR

def escreveTela():
    return print(f"""
    Salario Bruto: ======================== {salario}.
    (-) Sindicato (3%): =================== {sindicato}.
    (-) IR: ({taxa}%): ======================== {impostoRenda}.
    (-) INSS (10%): ======================= {inss}.
    FGTS (11%): =========================== {fgts}.
    Salário liquido ======================= {salarioTotal}.
    """)

def salarioLiquido(salario):
    descontos = (sindicato + inss + impostoRenda)
    return salario - descontos
    

try:
    preco_horas = float(input('Entre com o valor de horas trabalhadas por mes: '))
    qtd_horas_trabalhadas = float(input('Entre com o valor da hora: '))
except ValueError:
    print('Erro, Por favor digite apenas numeros!')
else:
    salario = salarioBruto(preco_horas, qtd_horas_trabalhadas)
    sindicato = descSindicato(salario)
    fgts = descFgts(salario)
    impostoRenda = descIR(salario)
    inss = descInss(salario)
    salarioTotal = salarioLiquido(salario)
    taxa = int(impostoRenda/salario * 100)
    escreveTela()





