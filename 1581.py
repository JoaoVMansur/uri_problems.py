teste  = int(input())

while teste != 0:
    linguas = []
    pessoas = int(input())
    for i in range(pessoas):
        lingua = input()
        linguas.append(lingua)

    check = all(i == linguas[0] for i in linguas)

    if check:
        print(linguas[0])
    else:
        print("ingles")

    teste -= 1
