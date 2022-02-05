i, n = map(int,input().split(" "))
banco = {"D": i, "E": i, "F": i}
for o in range(n):
    operacoes = [i for i in input().split()]
    if operacoes[0] == "A":
        banco[operacoes[1]] += int(operacoes[3])
        banco[operacoes[2]] -= int(operacoes[3])
    elif operacoes[0] == "C":
        banco[operacoes[1]] -= int(operacoes[2])
    elif operacoes[0] == "V":
        banco[operacoes[1]] += int(operacoes[2])

print(f"{banco['D']} {banco['E']} {banco['F']}")
