teste = int(input())

for i in range(teste):
    nr = input().split(" ")

    if nr[0][len(nr[0])-len(nr[1]):] == nr[1]:
        print("encaixa")
    else:
        print("nao encaixa")
