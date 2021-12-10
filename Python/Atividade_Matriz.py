'''
Declare uma matriz quadratica e preencha com x a sua diagonal
principal e com 0 os demais elementos. Escreva ao final
a matriz obtida. '''

print('Diagonal principal'.center(50))
num = int(input('Digita a quantidade de linha e colunas da matriz: '))

# gera a matriz
valor = []
for x in range(num):
    linha = []
    for y in range(num):

        linha.append(0)  # [0,0,0,0,0]
    valor.append(linha)

# edição da matriz
for p in range(num):
    for m in range(num):
        if p == m:
            valor[p][m] = '\033[35mx\033[m'


# impressão da matriz
for z in valor:
    for w in z:
        print(w, end=' ')
    print()
