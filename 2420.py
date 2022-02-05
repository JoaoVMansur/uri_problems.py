secao = int(input())

tamanho = [i for i in map(int,input().split())]

soma, area = 0, 0

a = len(tamanho)
for i,_ in enumerate(tamanho):
    if soma == sum(tamanho[i:a]):
        area = i
        break
    else:
        soma += tamanho[i]

print(area)
