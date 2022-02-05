operacao = input()
def matriz():
    matriz = []
    for l in range(12):
        linha = []
        for  c in range(12):
            n = float(input())
            linha.append(n)
        matriz.append(linha)
    return matriz
def media(matriz, operacao):
    media = 0
    fator = 1
    for i in range(len(matriz)):
        for v in range(fator, len(matriz[i])):
            media += matriz[i][v]
        fator += 1
    if operacao == "S":
        return media
    elif operacao == "M":

        return round(media/66, 1)


matriz = matriz()
media = media(matriz, operacao)
print(media)