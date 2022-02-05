input()
a = float(input())
b = float(input())

salario = a+(0.15*b)

salario = "{:.2f}".format(salario)

print(f"TOTAL = R$ {salario}")