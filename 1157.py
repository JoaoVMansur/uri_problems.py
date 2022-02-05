n = int(input())
def divisores(n):

    for x in range(1, n+1):
        if n%x == 0:
            print(x)


divisores(n)