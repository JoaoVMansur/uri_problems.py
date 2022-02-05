def vetor():
    vetor = []
    for i in range(100):
        n = float(input())
        vetor.append(n)
    return vetor

def formatar(vetor):
    novo_vetor = []
    indice = []
    indi = 0
    for i in vetor:
        if i <= 10:
            indice.append(indi)
            indi += 1
            i = "{:.1f}".format(i)
            novo_vetor.append(i)
        else:
            indi += 1
    return novo_vetor, indice

def mostrar(novo_vetor, indice):

    for i in range(0, len(novo_vetor)):
        print(f"A[{indice[i]}] = {novo_vetor[i]}")

vetor = vetor()
novo_vetor, indice = formatar(vetor)
mostrar(novo_vetor, indice)