teste = int(input())

for i in range(teste):
    m = 0
    v = 0

    m1, x, v1 = input().split()
    m2, x, v2 = input().split()
    m1 = int(m1)
    v1 = int(v1)
    m2 = int(m2)
    v2 = int(v2)
    if m1 > v1:
        m += 3
    elif m1 < v1:
        v += 3
    elif m1 == v1:
        m +=1
        v +=1

    if m2 > v2:
        m += 3
    elif m2 < v2:
        v += 3
    elif m2 == v2:
        m +=1
        v +=1


    if m > v:
        print("Time 1")
    elif m < v:
        print("Time 2")
    elif m == v:
        print("Penaltis")