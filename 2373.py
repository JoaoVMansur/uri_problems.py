bandeijas = int(input())

quebrados = 0
for i in range(bandeijas):

    l, c = map(int,input().split(" "))

    if l > c:
        quebrados += c
    else:
        quebrados += 0


print(quebrados)
