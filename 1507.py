teste = int(input())

def subsequencia(teste):

    for i in range(teste):

        seq = input()
        q = int(input())
        for i in range(q):
            sub = input()
            if sub in seq:
                print("YES")
            else:
                print("NO")

subsequencia(teste)