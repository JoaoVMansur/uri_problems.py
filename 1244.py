teste = int(input())

def ordenar(teste):

    for i in range(teste):

        frase = input().split()
        frase.sort(key=len, reverse=True)

        for i in range(len(frase)):
            if i+1 == len(frase):
                print(frase[i])
            else:
                print(frase[i], end=" ")


ordenar(teste)