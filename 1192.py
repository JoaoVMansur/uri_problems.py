teste = int(input())


def game(teste):

    for i in range(teste):
        resultado = 0
        partida = input()

        if int(partida[0]) == int(partida[2]):
            resultado = int(partida[0])**2

        elif partida[1].isupper():
            resultado = int(partida[2]) - int(partida[0])

        elif partida[1].islower():
            resultado = int(partida[0])+int(partida[2])


        print(resultado)

game(teste)