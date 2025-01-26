from datetime import datetime, timezone
from pprint import pprint


print(datetime.now())

#Extraindo apenas a data de um objeto datetime
print(f'Extrai apenas a data: {datetime.now().date()}')

#Retornando o dia de um objeto datetime
print(f'Retornando o dia: {datetime.now().day}')

#Retornando o mês de um objeto datetime
print(f'Retorna o mês: {datetime.now().month}')

#Retorna apenas o ano de um objeto datetime
print(f'Retorna apenas o ano: {datetime.now().year}')

#Extraindo apenas a hora de um objeto datetime
print(datetime.now().time())

#Retornando a hora de um objeto datetime
print(f'Retornando a hora de um objeto datetime: {datetime.now().hour}')

print('---------------------------------------------------------------------')

print(datetime.now(timezone.utc).dst())


print('-----------------Retorna o dia atual da semana, 1 para segunda e 7 para domingo--------------------------')
print(datetime.now().isoweekday())

print(datetime.now().strftime("%H:%M:%S"))

# timetz()
# Retorna apenas a parte de tempo com informações de fuso horário.

print(datetime.now().timetz())