teste = int(input())

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto = [i.upper() for i in alfabeto]


while teste != 0:
    teste -= 1
    palavra = input()
    codigo = int(input())
    n_p = ""
    for i in palavra:
        if i in alfabeto:
            posicao = alfabeto.index(i) - codigo
            n_p += alfabeto[posicao]

    print(n_p)

