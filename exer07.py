dist = [
[0,15,30,5,12],
[15,0,10,20,28],
[30,10,0,25,18],
[5,20,25,0,14],
[12,28,18,14,0]
]

l = int(input("Cidade origem: "))
c = int(input("Cidade destino: "))

print("Distância:", dist[l][c], "km")

total = 0

for i in range(6):
l = int(input("Linha: "))
c = int(input("Coluna: "))

total += dist[l][c]

print("Total percorrido:", total, "km")