a, g, ka, kg = map(float,input().split(" "))

pa = ka/a
pg = kg/g

if pa > pg:
    print("A")
elif pg > pa:
    print("G")
elif pa == pg:
    print("G")