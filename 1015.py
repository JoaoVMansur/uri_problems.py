x1,y1 = map(float,input().split(" "))
x2,y2 = map(float,input().split(" "))

distancia = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
distancia = "{:.4f}".format(distancia)
print(distancia)
