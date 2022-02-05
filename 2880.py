def cp(x, y):
    for i in range(len(x)):
        if x[i] == y[i]: return False
    return True

msg = input()
crib = input()

espaco = len(msg)-len(crib)+1
t = len(crib)
posicao = 0

for i in range(espaco):

    if cp(msg[i:t+i], crib): posicao +=1

print(posicao)