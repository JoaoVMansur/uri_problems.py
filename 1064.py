numeros = []
positivos = 0
for i in range(6):
    a = float(input())
    if a > 0:
        numeros.append(a)

for i in numeros:
    if i > 0:
        positivos += 1

media = sum(numeros)/len(numeros)
media = "{:.1f}".format(media)
print(f"{positivos} valores positivos")
print(media)