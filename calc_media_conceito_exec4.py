def calcMedia(n1, n2):
    return (n1+n2)/2

def conceito(media):
    conceito = ''
    if media <= 4: conceito = 'E'
    if media > 4 and media <= 6: conceito = 'D'
    if media > 6 and media <= 7.5: conceito = 'C'
    if media > 7.5 and media <= 9: conceito = 'B'
    if media > 9 and media <= 10: conceito = 'A'

    return conceito

def aprovado(valor):
    if valor == 'A' or valor == 'B' or valor == 'C':
        situacao = 'Aprovado'
    elif valor == 'D' or valor == 'E':
        situacao = 'Reprovado'

    return situacao


try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
except ValueError:
    print('Erro!')
else:
    media = calcMedia(nota1, nota2)
    conceito = conceito(media)
    situacao = aprovado(conceito)

    print(f"""
    Media ======= {media}
    Conceito ======= {conceito}
    Situação ======= {situacao}""")