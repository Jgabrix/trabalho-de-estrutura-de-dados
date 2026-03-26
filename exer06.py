import random

cartela = []
numeros_usados = []

for i in range(5):
linha = []
for j in range(5):
while True:
num = random.randint(0, 99)
if num not in numeros_usados:
numeros_usados.append(num)
linha.append(num)
break
cartela.append(linha)

Exibir cartela

for linha in cartela:
for num in linha:
print(f"{num:2}", end=" ")
print()