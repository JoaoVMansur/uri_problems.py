n, m = map(int,input().split())
minhocas = []
for l in range(n):
    linha = [i for i in map(int,input().split())]
    minhocas.append(linha)
maior = 0
for l in minhocas:
    soma = 0
    for c in range(len(l)):

        soma += l[c]
    if soma > maior:
        maior = soma
for l in range(len(minhocas[0])):
    sum = 0
    for c in range(len(minhocas)):
        sum += minhocas[c][l]

    if sum > maior:
        maior = sum
print(maior)