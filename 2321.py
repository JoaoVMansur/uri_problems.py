p1 = [int(i) for i in input().split()]
p2 = [int(i) for i in input().split()]


if p1[2] > p2[0] and p1[3] > p2[1]:
    print(1)
else:
    print(0)