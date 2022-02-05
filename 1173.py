n = int(input())

def vetor(n):
    vetor = []

    for i in range(10):
        if i == 0:
            vetor.append(n)
        else:
            vetor.append(vetor[i-1]*2)

    return vetor

def mostrar(vetor):

    for i in range(0, len(vetor)):
        print(f"N[{i}] = {vetor[i]}")
vetor = vetor(n)
mostrar(vetor)