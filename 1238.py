teste = int(input())

def misturar(teste):
    def menor_palavra(palavra):
        menor = palavra[0]
        for i in palavra:
            if len(i) < len(menor):
                menor = i
        return menor
    for i in range(teste):

        palavras = ""

        palavra = input().split(" ")
        menor_p = menor_palavra(palavra)

        for i in range(len(menor_p)):
            palavras += palavra[0][i]+palavra[1][i]
        if palavra.index(menor_p) == 0:

            palavras += palavra[1][len(menor_p):]
        else:
            palavras += palavra[0][len(menor_p):]

        print(palavras)


misturar(teste)