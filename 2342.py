
maximo = int(input())

n1, o, n2 = map(str,input().split(" "))

resultado = 0
if o == "+":
    resultado += int(n1) + int(n2)

elif o == "*":
    resultado += int(n1) * int(n2)


if resultado > maximo:
    print("OVERFLOW")

else:
    print("OK")