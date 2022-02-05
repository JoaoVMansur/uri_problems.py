def vetor():
    vetor = []

    for i in range(20):
        n = int(input())
        vetor.append(n)

    return vetor

def trocar(vetor):
    comeco = 0
    for i in range(len(vetor)//2):
        vetor[comeco], vetor[-(comeco+1)] = vetor[-(comeco+1)], vetor[comeco]
        comeco += 1
    return vetor

def formatar(vetor):
    for i in range(0, len(vetor)):

        print(f"N[{i}] = {vetor[i]}")

vetor = vetor()
trocado = trocar(vetor)
formatar(trocado)