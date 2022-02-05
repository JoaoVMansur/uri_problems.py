cartas = list(map(int,input().split(" ")))

crescente = []

for i in cartas:
    crescente.append(i)

crescente.sort()

if cartas == crescente:
    print("C")
elif cartas == crescente[::-1]:
    print("D")
else:
    print("N")
