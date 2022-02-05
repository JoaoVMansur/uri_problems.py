


def fibonacci(n):
    vetor = []
    valor = 0
    for i in range(n+1):
        if len(vetor) < 2:
            vetor.append(valor)
            valor += 1
        else:
            valor = vetor[-1] + vetor[-2]
            vetor.append(valor)

    return vetor

def mostrar(m, vetor):

    print(f"Fib({m}) = {vetor[-1]}")

n = int(input())

for i in range(n):
    m = int(input())
    vetor = fibonacci(m)
    mostrar(m, vetor)