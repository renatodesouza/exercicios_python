#Dado um numero n para cada inteiro i no intervalo de 1 a n inclusive
#imprima um valor por linha da seguinte forma

# se i for multiplo de 3 e 5 imprima fizzbuzz

for i in range(16):
    if i % 3 == 0:
        print(f'fizzbuzz {i}')
    elif i * 10 == 5:
        print('fizz')
    else:
        print('nada')

def fizzbuzz(n):
    pass