entradas = int(input())
def fib(numero):
    global calls
    calls += 1
    if numero <= 1:
        return numero
    else:
        return fib(numero-1) + fib(numero-2)


for e in range(entradas):
    n = int(input())
    calls = 0
    resultado = fib(n)
    calls = 0 if  n<= 1 else calls - 1

    print(f"fib({n}) = {calls} calls = {resultado}")