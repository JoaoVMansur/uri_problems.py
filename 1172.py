def vetor():
    vetor = []

    for i in range(10):
        n = int(input())
        vetor.append(n)

    return vetor

def formatar(vetor):

    for valor in range(0, len(vetor)):
        if vetor[valor] <= 0 :
            vetor[valor] = 1

    return vetor

def mostrar(vetor):

    for valor in range(0, len(vetor)):
        print(f"X[{valor}] = {vetor[valor]}")


vetor = vetor()
formatado = formatar(vetor)
mostrar(formatado)