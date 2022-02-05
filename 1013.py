lista = []

a,b,c = map(int,input().split())

lista.append(a)
lista.append(b)
lista.append(c)

maior = max(lista)

print(f"{maior} eh o maior")