# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

import random

temperatura = [round(random.uniform(20, 36)) for _ in range(12)]

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
          'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

media_anual = round(sum(temperatura) / len(temperatura))

print(f'A média anual da temperatura é: {media_anual}')

for i in range(len(temperatura)):
    if temperatura[i] > media_anual:
        print(f'{i + 1} - {meses[i]} - {temperatura[i]}')

