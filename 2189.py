teste = 1
n = 1
while n != 0:
    n = int(input())

    if n == 0:
        n = 0
    else:

        sorteio = [int(x) for x in input().split()]
        ganhador = 0
        for i in range(len(sorteio)):
            if sorteio[i] == i+1:
                ganhador += sorteio[i]


        print(f"Teste {teste}")
        print(ganhador)
        print()
        teste += 1