ler gabarito

gabarito = []
for i in range(10):
resp = input(f"Gabarito questão {i+1}: ")
gabarito.append(resp)

para 3 alunos

for aluno in range(3):
print(f"\nAluno {aluno+1}")

matricula = int(input("Matrícula: "))  
  
respostas = []  
acertos = 0  

# ler respostas do aluno  
for i in range(10):  
    r = input(f"Resposta questão {i+1}: ")  
    respostas.append(r)  
      
    if r == gabarito[i]:  
        acertos += 1  

# calcular nota  
nota = acertos  
percentual = (nota / 10) * 100  

print("Respostas:", respostas)  
print("Nota:", nota)  
print("Percentual:", percentual, "%")  

if nota >= 7:  
    print("Aprovado")  
else:  
    print("Reprovado")