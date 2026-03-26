mat = [
 [8,0,7],
 [4,5,6],
 [3,10,2]
]

soma = sum(mat[0])
ok = True

# verificar linhas
for i in range(3):
    if sum(mat[i]) != soma:
        ok = False

# verificar colunas
for j in range(3):
    if mat[0][j] + mat[1][j] + mat[2][j] != soma:
        ok = False

# diagonais
if mat[0][0] + mat[1][1] + mat[2][2] != soma:
    ok = False

if mat[0][2] + mat[1][1] + mat[2][0] != soma:
    ok = False

# resultado
if ok:
    print("É quadrado mágico")
else:
    print("Não é quadrado mágico")