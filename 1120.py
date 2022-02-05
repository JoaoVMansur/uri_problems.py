a = 1
b = 1

while a != 0 and b != 0:
    a, b = map(int, input().split(" "))
    if a == 0 and b == 0:
        a = 0
        b = 0
    else:
        numero = []
        for i in str(b):
            if str(a) != i:
                numero.append(i)

        if numero == []:
            print(0)
        else:

            for i in range(len(numero)):
                numero[i] = int(numero[i])
            for i in range(len(numero)):
                if a == numero[i]:
                    numero.remove(numero[i])
            strings = [str(num) for num in numero]
            num_str = int("".join(strings))
            print(num_str)


