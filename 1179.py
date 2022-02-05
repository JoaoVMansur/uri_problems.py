def vetores():
    par = []
    impar = []

    for i in range(15):
        n = int(input())
        if len(par) < 5 and n % 2 == 0:
            par.append(n)
        elif len(impar) < 5 and n % 2 != 0:
            impar.append(n)
        else:
            if len(par) == 5:
                for i in range(len(par)):
                    print(f"par[{i}] = {par[i]}")
                par = []
            elif len(impar) == 5:
                for i in range(len(impar)):
                    print(f"impar[{i}] = {impar[i]}")
                impar = []
            if n % 2 == 0:
                par.append(n)
            elif n % 2 != 0:
                impar.append(n)

    for i in range(len(impar)):
        print(f"impar[{i}] = {impar[i]}")
    for i in range(len(par)):
        print(f"par[{i}] = {par[i]}")

vetores()