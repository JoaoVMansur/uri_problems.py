R = input()
G = input()
B = input()

if int(R, 16) < int(G, 16):
    total = 1
else:
    verde = (int(R, 16) // int (G, 16))**2
    azul = ((int (G, 16) // int (B, 16))**2)*verde
    total = verde + azul + 1


total = hex(total)

print(total[2:])

