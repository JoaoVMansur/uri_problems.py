c1, c2 = map(int,input().split(" "))

c3 = 0

if c1 == c2:
    c3 = c1
else:
    maior = c1 if c1 > c2 else c2
    menor = c2 if c2 < c1 else c1

    c3 = maior

print(c3)
