a, b, c, d = map(int,input().split(" "))

maior_1 = c if c > a else a
menor_1 = a if a < c else c
maior_2 = d if d > b else b
menor_2 = b if b < d else d



cruzamento = (maior_1 - menor_1) + (maior_2 - menor_2)

print(cruzamento)