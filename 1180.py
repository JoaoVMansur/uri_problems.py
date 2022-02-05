tamanho = int(input())
vetor = [int(x) for x in input().split()]

def pegar_menor(vetor):
    menor = min(vetor)
    indice = vetor.index(menor)
    return menor, indice


menor, indice = pegar_menor(vetor)


print(f"Menor valor: {menor}")
print(f"Posicao: {indice}")