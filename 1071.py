a = int(input())
b = int(input())

maior = a if a>b else b
menor = b if b<a else a
soma = 0

for n in range(menor+1, maior):

    if n%2 != 0:
        soma += n


print(soma)

