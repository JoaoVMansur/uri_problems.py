n = int(input())
In = 0
out = 0
for x in range(n):
    a = int(input())
    if a >= 10 and a <= 20:
        In += 1

    else:
        out += 1


print(f"{In} in\n{out} out")
