import calendar
from datetime import datetime, date


# Descubra se uma data é bissexta:

# Crie uma função que receba um ano como entrada e retorne se ele é ou não bissexto. Use o módulo calendar para isso.

def ano_bissexto(ano):
    return f'O ano é bissexto. ' \
        if calendar.isleap(ano) else f'o ano não é bissexto.'


while True:
    try:
        ano = int(input("Informe um ano para verificar se o mesmo é bissexto. "))
        break
    except ValueError:
        print('Informe uma data valida, exemplo 2024')


print(ano_bissexto(ano))

