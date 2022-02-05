testes = int(input())

while testes != 0:
    ganhadores = []
    j1 = 0
    j2 = 0
    for i in range(testes):
        a, b = map(int,input().split(" "))
        if a > b:
            j1 += 1

        elif b > a:
            j2 +=1

    ganhadores.append(j1)
    ganhadores.append(j2)

    print(f"{ganhadores[0]} {ganhadores[1]}")

    testes = int(input())