n, m = map(int,input().split())

h = [i for i in map(int,input().split())]

movimentos = 0

for i in range(len(h)):

    while h[i] != m:
        if h[i] < m:
            h[i] += 1
            h[i+1] +=1
            movimentos += 1
        elif h[i] > m:
            h[i] -= 1
            h[i + 1] -= 1
            movimentos += 1

print(movimentos)