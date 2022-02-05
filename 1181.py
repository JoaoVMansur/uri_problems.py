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


def pegar_linha(matriz, indice):
    linha = []
    for valor in matriz[indice]:
        linha.append(valor)

    return linha

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
linha = pegar_linha(matriz, indice)
media = media_soma(linha, operacao)

print(media)