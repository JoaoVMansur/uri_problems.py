from math import floor, sqrt


def joseph(n):
    if n == 1:
        return print(n)
    lista = [i for i in range(1, n + 1)]
    k = calcula_primos(n)
    remover = (k[0] % len(lista)) - 1
    lista.remove(lista[remover])
    for contador in range(1, n - 1):
        remover = (k[contador] % len(lista) - 1 + remover) % len(lista)
        lista.remove(lista[remover])
    return print(lista[0])


def calcula_primos(n):
    primos = []  # temos que incluir 0 pois ele vai contar até o 2 primeiro
    # for num in range(3, 100000):
    num = 2
    while len(primos) < n - 1:
        if verifica_primo(num):
            primos.append(num)
        num += 1
    return primos


def verifica_primo(n):

    for valor in range(2, floor(sqrt(n)) + 1):
        if n % valor == 0:
            return False
    return True


n = int(input())
while n != 0:

    joseph(n)
    n = int(input())