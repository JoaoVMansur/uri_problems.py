a,b,c = map(int, input().split(" "))

numeros = [a, b, c]

numeros.sort()

for n in numeros:
    print(n)
print()
print(f"{a}\n{b}\n{c}")
