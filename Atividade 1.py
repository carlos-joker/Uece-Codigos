'''Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade. Para cada casa visitada foi fornecido 
o número do canal (2, 4, 6, 7, 9, 13) e o número de pessoas que estavam assistindo a ele naquela casa.

Fazer um programa que:

·       leia um número indeterminado de dados, sendo que canal 0 (zero) representa fim da entrada de dados;
       
·       calcule a percentagem de audiência para cada emissora;
       
·       imprima total de pessoas pesquisadas, total de pessoas por canal e sua respectiva percentagem.'''


import time

lista2 = []
lista4 = []
lista6 = []
lista7 = []
lista9 = []
lista13 = []
pc2 = 0
pc4 = 0
pc6 = 0
pc7 = 0
pc9 = 0
pc13 = 0

def menu():
    a = 1 
    while a == 1:
        x = int(input('Digite o canal que você mais assite: 1-Globo 2-Record 3-SBT 4-CNN 5-Band 6-Discovery Channel 0-Sair'))
        time.sleep(1.5)
        if x == 1:
            lista2.append(1)
            print('Voto computado!!!')  
            time.sleep(0.5)      


        elif x == 2:
            lista4.append(1)
            print('Voto computado!!!') 
            time.sleep(0.5)      


        elif x == 3:
            lista6.append(1)
            print('Voto computado!!!')  
            time.sleep(0.5)      


        elif x == 4:
            lista7.append(1)
            print('Voto computado!!!')
            time.sleep(0.5)      


        elif x == 5:
            lista9.append(1)
            print('Voto computado!!!') 
            time.sleep(0.5)      


        elif x == 6:
            lista13.append(1) 
            print('Voto computado!!!') 
            time.sleep(0.5)      


        elif x == 0:
            a = 0
            print('Encerrando...')  
            time.sleep(1.5) 
            return audiencia()     

        else:
            print('Opção Inválida!!!')

def audiencia():
    global pc2
    global pc4
    global pc6
    global pc7
    global pc9
    global pc13
    

    total = sum(lista2 + lista4 + lista6 + lista7 + lista9 + lista13)
    
    print('O total de pessoas consultadas nessa pesquisa foram {}'.format(total))
    time.sleep(2)
    print('Calculando..........')


    
    pc2 =(sum(lista2)/total)*100
    pc4 =(sum(lista4)/total)*100
    pc6 =(sum(lista6)/total)*100
    pc7 = (sum(lista7)/total)*100
    pc9 = (sum(lista9)/total)*100
    pc13 = (sum(lista13)/total)*100
    

    return imprimir()

def imprimir():
    global pc2
    global pc4
    global pc6
    global pc7
    global pc9
    global pc13
    print('O total de pessoas que sao audiência do canal 2 são {:.2f}% dos pesquisados'.format(pc2))
    print('O total de pessoas que sao audiência do canal 4 são {:.2f}% dos pesquisados'.format(pc4))
    print('O total de pessoas que sao audiência do canal 6 são {:.2f}% dos pesquisados'.format(pc6))
    print('O total de pessoas que sao audiência do canal 7 são {:.2f}% dos pesquisados'.format(pc7))
    print('O total de pessoas que sao audiência do canal 9 são {:.2f}% dos pesquisados'.format(pc9))
    print('O total de pessoas que sao audiência do canal 13 são {:.2f}% dos pesquisados'.format(pc13))




menu()




