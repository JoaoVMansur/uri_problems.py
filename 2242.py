vogais = ["a", "e", "i", "o", "u"]

risada = list(input())
risadas = []

for i in risada:
    if i in vogais:
        risadas.append(i)

normal = ""
invertida = ""
for i in risadas:
    normal += i
for i in reversed(risadas):
    invertida += i


if normal == invertida:
    print("S")
else:
    print("N")