
def pegar_notas():

    notas = []
    while len(notas) != 2:
        n = float(input())
        if n <= 10 and n >= 0:
            notas.append(n)
        else:
            print("nota invalida")
    return notas
def media(pegar_notas):
    media = 0
    for i in pegar_notas:
        media += i

    media = media/2
    return media
media = media(pegar_notas())
print(f"media = {media}")