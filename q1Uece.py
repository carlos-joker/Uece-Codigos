#Questao 1
def somar():
    aux = 0
    for i in range(101):
        aux = aux + i

        i +=1
    print('A soma dos termos de (1 + 2 + 3 + ... + 99 + 100 é {}'.format(aux))
somar()

#questao 2

a = input('Digite 30 valores aleatorios e separados por virgula: ')

lista = list(map(float, a.split(',')))

o = []
for i in lista:
    if i >= 0:
        o.append(1)
    else:
        o.append(0)
    i = i + 1

print(o)