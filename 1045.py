a,b,c = map(float, input().split(" "))
lados =[a, b, c]
lados.sort()

a = max(lados)
b = lados[1]
c = lados[0]
if a > b+c:
    print("NAO FORMA TRIANGULO")

if a**2 == b**2+c**2:
    print("TRINAGULO RETANGULO")

if a**2 > b**2+c**2:
    print("TRIANGULO OBTUSANGULO")

if a**2 < b**2+c**2:
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRINAGULO EQUILATERO")

if a == b or b==c or a==c:
    print("TRINAGULO ISOSCELES")