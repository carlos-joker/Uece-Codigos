import time
#questao 1
def somar():
    aux = 0
    for i in range(101):
        aux = aux + i

        i +=1
    print('A soma dos termos de (1 + 2 + 3 + ... + 99 + 100) é {}'.format(aux))
somar()

#questao 2 
x = int(input('Digite um numero: '))

lista = []

for i in range(1, x + 1):
    
    lista.append(i)
    i = i + 1
print(lista)

print('A soma total de 1 até {} é {}'.format(x, sum(lista)))

#questao 3
b = 0
while b == 0:
    x = int(input('Digite o valor que deseja saber a taboada: '))
    a = 0
    while a == 0:
        y = int(input('Digite a operação desejada: 1- Somar 2-Subtrair 3-Multiplicar 4-Dividir'))

        if y == 1:
            for i in range(1, 11):
                print('{} + {} = {}'.format(x, i, x + i))
                i =+ 1
                a = 1
        elif y == 2:
            for i in range(1, 11):
                print('{} - {} = {}'.format(x, i, x - i))
                i =+ 1
                a = 1
        elif y == 3:
            for i in range(1, 11):
                print('{} * {} = {}'.format(x, i, x * i))
                i =+ 1
                a = 1
        elif y == 4:
            for i in range(1, 11):
                print('{} / {} = {}'.format(x, i, x / i))
                i =+ 1
                a = 1
        else:
            print('Opção Inválida!!!')

    z = input('Deseja realizar a operação novamente?: (s/n)') 
    if z == 's':
        print('Reiniciando...')
        time.sleep(0.5)
    else:
        b = 1
        print('Encerrando...')
        time.sleep(0.5)

#questao 4
ini = 0
lista = []
y = int(input('Digite quantos numeros compoem a media: '))
while ini <= y-1:
    n = float(input('Digite o número: '))
    time.sleep(0.5)
    lista.append(n)
    ini += 1
        
soma = sum(lista)


print('A média aritimética é {}'.format(soma / y))

#questao 5

a = 0 
while a == 0:
    sal = float(input('Digite o seu salario atual : R$ '))

    if sal < 500:
        r = 15
        reajuste = sal * (15/100)
    elif sal > 500 and sal <= 1000:
        r = 10
        reajuste = sal * (10 / 100)
    else:
        r = 5
        reajuste = sal * (5 / 100)

    print('O seu salario atual é R${:.2f}, com o reajuste de {}% seu novo salário será R${:.2f}'.format(sal, r, sal+reajuste))

    z = input('Deseja realizar o procedimento novamente?: (s/n)')
    if z == 's':
        print('Reiniciando...')
        time.sleep(0.5)
    else:
        print('Encerrando...')
        time.sleep(0.5)
        a = 1