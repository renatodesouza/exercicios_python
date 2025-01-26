# Faça um programa que peça um número inteiro e determine
#  se ele é ou não um número primo. Um número primo é aquele
#  que é divisível somente por ele mesmo e por 1.


numero = int(input("Informe um numero para verificar se é um numero primo: "))



cont = 0

for i in range(numero, 0, -1):
    if numero % i == 0:
        cont += 1

if cont == 2:
    print("O numero é primo")
else:
    print("O numero nao é primo")

def conta(valor):
    if valor == 2:
        return 'primo'
    return 'nao primo'

lst = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 30, 31, 37, 41, 42, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

cont = 0

primos = {}

for i in range(0, len(lst)):
    for n in range(lst[i], 0, -1):
        if lst[i] % n == 0:
            cont += 1

    if cont == 2:
        primos[lst[i]] = 'primo'
        cont = 0
    else:
        primos[lst[i]] = 'não primo'
        cont = 0

print(primos)

