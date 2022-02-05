notas = [100, 50, 20, 10, 5, 2, 1]

valor = int(input())
print(valor)
for x in notas:
    q = int(valor/x)
    valor = valor-(q*x)
    print(f"{q} nota(s) de R$ {x},00")
