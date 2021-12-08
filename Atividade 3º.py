
from os import system
from time import sleep                        # biblioteca de system 


Senha_Atual = 1994
comando = True

while (comando != True):

    
    system('cls')

    print('\t._______________________________________.')
    print('\t|    >>> Classificação de alunos <<     |')
    print('\t|                                       |')
    print('\t| Opção:                                |')
    print('\t|                                       |')
    print('\t| F - Feminino                          |')
    print('\t| M - Masculino                         |')
    print('\t|                                       |')
    print('\t|_______________________________________|')

    sexo = input('\nDigita a opção: ')
    nome = str (input('Digita seu nome completo: '))
    senha = input('Digita a senha: ')
     
    if (senha == Senha_Atual) or (comando == True):
      

#----------(fim de while)-------------------------------                                                         
     
         if (sexo == 'M') or (sexo == 'm'):                                          # se a codição for igual a (M) ou (m)

             print('\nOlá {} você e do gênero Masculino ({})\n'.format(nome,sexo))   # imprimir na tela 

         elif (sexo == 'F') or (sexo == 'f'):                                        # se a codição for igual a (M) ou (m)

             print('\nOlá {} você e do gênero Feminino ({})\n'.format(nome,sexo))    # impimir na tela 
         else:
             print('\nSexo Inválido !')  
         comando == False                                                   # se não sexo invalido 
            
              

     
     



















