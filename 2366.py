n, m = map(int, input().split())

postos = [i for i in input().split()]
postos = [int(i) for i in postos]

maratona = 0
for i in range(len(postos)-1):
    if postos[i+1] - postos[i] > m:

        maratona += 1
    elif postos[-1] + m < 42195:
        maratona += 1

if maratona == 0:
    print("S")
else:
    print("N")