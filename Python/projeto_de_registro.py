
from os import  system
from time import sleep

apagar_tela = 'cls'  # ou clear
alunos = {}
print('Registro de alunos do curso de Python')
print('Prof: Everton Batman ')
print('-='*50)

while True:
    print('''
     Menu:
     
     1 - Ver a lista de alunos matriculados.
     2 - Adicionar um aluno a lista.
     3 - Ver registro do curso de um aluno. 
     4 - Sair''')

    opcao = (input('\nDigita o numero da operação que deseja executar: '))

    if(opcao == "1"):
        if not alunos:
            system(apagar_tela)
            print('...Não há alunos registrados !....'.center(50))
            for x in range(5):
                sleep(1)
            system(apagar_tela)

        else:

            print('Lista de alunos: ')
            for nome, cursos in alunos.items():
                if(alunos != alunos):
                    print(f'{nome} - {cursos} cursos')
                else:
                    system(apagar_tela)
                    del(alunos[1:4])
                    print(alunos)
                    print('Cursos não existe !')

                    for x in range(5):
                        sleep(1)
                system(apagar_tela)

    elif(opcao == "2"):
        system(apagar_tela)
        print('''
        opção de cursos:
        
        1 - Python
        2 - JavaScript
        3 - java
        4 - Programação C
        5 - Aduino ''')

        nome = str(input('\nInsira o  nome: '))
        cursos = int(input('Insira o numero do curso: '))
        alunos[nome] = cursos
        system(apagar_tela)

    elif(opcao == "3"):
        system(apagar_tela)
        nome = str(input('\nInsira o nome: '))
        if nome in alunos:

            if(cursos >= 1) and (cursos <= 5):
                system('cls')
                print('\n{} Esta matriculado !'.format(nome))
                print(f'Cursos: {alunos[nome]} Python')
                for x in range(5):
                    sleep(1)
                system(apagar_tela)

            else:
                print('...Cursos não existe !...')

        else:
            print(f'Não existe aluno com esse nome: {nome}')

    elif(opcao == "4"):
        system(apagar_tela)
        print('...Saindo do System...'.center(65))
        for x in range(22):
            print(' -', end=' ')
            sleep(1)
        break

    else:
        print('Opção errada, Digita novamente!')
