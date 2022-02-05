teste = int(input())

def numeros(teste):
    numeros = []
    for i in range(teste):
        n = int(input())
        numeros.append(n)
    numeros.sort()
    return numeros

def contar(numeros):
    contados = []
    conta = []
    for i in numeros:
        valor = numeros.count(i)
        if i in contados:
            None
        else:
            conta.append(valor)
            contados.append(i)

    return contados, conta

numeros = numeros(teste)
numeros, quantidade = contar(numeros)

for i in range(0, len(numeros)):

    print(f"{numeros[i]} aparece {quantidade[i]} vez(es)")