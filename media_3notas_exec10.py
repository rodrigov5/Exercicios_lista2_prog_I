nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
nota3 = float(input('Entre com a terceira nota: '))

media = 0
final = ''

def calcMedia(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def situacao(m):
    if m >= 7 and m < 10:
        return 'Aprovado'
    elif m < 7:
        return 'Reprovado'
    elif m == 10:
        return 'Aprovado Perfeitamente 👌'
    
final = situacao(media)
media = calcMedia(nota1, nota2, nota3)

print(f'Você foi {final}, Media {media: .1f}')