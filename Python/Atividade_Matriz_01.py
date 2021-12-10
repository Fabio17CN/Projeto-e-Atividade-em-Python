
# Crie uma matriz de 2 x 3 para pedir e guardar nome de e depois imprima os nomes na tela

print('\n> Matriz 2 x 3 para guarda nomes <\n')
matriz = [[0, 0, 0], [0, 0, 0]]
for x in range(0, 2):

    for y in range(0, 3):

        matriz[x][y] = str(input('{} º Digita nome: '.format(y+1)))


print('-='*30)
for x in range(0, 2):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^8}]', end=' ')
    print()
