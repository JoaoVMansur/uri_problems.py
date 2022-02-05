hi,mi,hf,mf = map(int, input().split(" "))

hora = hf-hi
minuto = mf-mi

if minuto < 0:
    minuto += 60
    hora -= 1
    if hora < 0:
        hora += 24


if hora == 0 and minuto == 0:
    hora = 24
    minuto = 0

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")