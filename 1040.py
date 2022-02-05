a,b,c,d = map(float,input().split(" "))


media = ((a*2)+(b*3)+(c*4)+(d))/(10)
2
print(f"Media: {round(media, 1)}")
if media >= 7:
    print("Aluno aprovado.")

elif media < 7 and media >= 5:
    print("Aluno em exame.")
    exame = float(input())
    media = (media+exame)/2
    print(f"Nota do exame: {exame}")
    if media >= 5:
        media = "{:.1f}".format(media)
        print("Aluno aprovado.")
        print(f"Media final: {media}")
    else:
        print(f"Media final: {media}")
        print("Aluno reprovado.")
else:
    media = "{:.1f}".format(media)
    print("Aluno reprovado.")