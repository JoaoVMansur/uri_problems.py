indice = int(input())
operacao = input()
def matriz():
    matriz = []
    for l in range(12):
        linha = []
        for  c in range(12):
            n = float   (input())
            linha.append(n)
        matriz.append(linha)

    return matriz


def pegar_coluna(matriz, indice):
    coluna = []
    for v in range(len(matriz)):
        valor = matriz[v][indice]
        coluna.append(valor)

    return coluna

def media_soma(linha, operacao):
    resultado = 0
    for valor in linha:
        resultado += valor
    if operacao == "S":
        resultado = resultado
    elif operacao == "M":
        resultado = resultado/12
    resultado = "{:.1f}".format(resultado)

    return resultado


matriz = matriz()
coluna = pegar_coluna(matriz, indice)
media = media_soma(coluna, operacao)

print(media)