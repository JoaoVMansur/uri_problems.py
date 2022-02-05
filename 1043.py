a, b, c = map(float, input().split(" "))

perimetro = a+b+c
area = ((a+b)*c)/2

if b-c < a and a < b+c and a-c < b and b < a+c and a-b < b and b < a+c:
    print(f"Perimetro = {perimetro}")
else:
    print(f"Area = {area}")