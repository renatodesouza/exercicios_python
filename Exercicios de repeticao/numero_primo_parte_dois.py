# Faça um programa que peça um número inteiro e determine
#  se ele é ou não um número primo. Um número primo é aquele
#  que é divisível somente por ele mesmo e por 1.

# Reduzir o intervalo do laço: Você está iterando de numero até 0, 
# mas só precisa verificar de 1 até a raiz quadrada de numero 
# para determinar se ele é primo. Isso reduzirá o número de operações.

import math

n = 29

cont = 0

rq = int(math.sqrt(n))

for i in range(1, rq + 1):
    if n % 2 == 0:
        cont += 1
    if cont > 2:
        print(f'{n} não é um número primo.')
        break

if cont == 2:
    print('é primo')
