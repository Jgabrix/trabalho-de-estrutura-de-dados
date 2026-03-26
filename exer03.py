vetor = [int] * 8


for i in range(len(vetor)):
    vetor[i] = int(input("Valor: "))


print()
valorX = int(input("Digite o valor de X de 0 a 7: "))
valorY = int(input("Digite o valor de Y de 0 a 7: "))


soma = vetor[valorX] + vetor[valorY]

print("O resultado da soma das posição de X e Y do vetor: ", soma)

