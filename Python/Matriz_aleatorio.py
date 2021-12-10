import random
import numpy as np

matrix = []
valores = list(np.arange(1, 100))

print('Gerador de matriz\n')
z = int(input('Quantidade de linhas: '))
x = int(input('Quantidade de colunas: '))
print()

for l in range(0, x):
    subMatriz = []

    for c in range(0, z):
        i = random.randint(0, len(valores)-1)
        num = valores[i]
        valores.pop(i)
        subMatriz.append(num)
    matrix.append(subMatriz)

for l in range(0, x):
    for c in range(0, z):
        print(f'[{matrix[l][c]:^5}]', end=' ')
    print()
