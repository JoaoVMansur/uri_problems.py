l = int(input())
c = int(input())

casa = 0

if l % 2 == 0 and c % 2 ==0:
    casa = 1
elif l % 2 != 0 and c % 2 != 0:
    casa = 1
else:
    casa = 0

print(casa)