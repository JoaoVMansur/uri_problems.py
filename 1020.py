dias = int(input())

periodos = [365, 30, 1]
calendario = []
for x in periodos:
    a = int(dias/x)
    calendario.append(a)
    dias -= a*x

print(f"{calendario[0]} ano(s)\n{calendario[1]} mes(es)\n{calendario[2]} dia(s)")
