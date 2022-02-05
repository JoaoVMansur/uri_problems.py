lista = []
def seq(numero):
        global lista
        lista.append(numero)
        while numero != 1 and numero !=0:

            if numero%2 == 0:
                numero = numero/2
                lista.append(numero)

            elif numero%2 != 0:
                numero = (numero*3)+1
                lista.append(numero)

entrada = 1
while entrada != 0:
    entrada = int(input())
    seq(entrada)
    if entrada == 0:
        lista = []
    else:
        print(int(max(lista)))
