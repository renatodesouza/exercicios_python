from datetime import date

#criando a data atual

hoje = date.today()

print(hoje)

#Criando uma data especifica

data_especifica = date(2024, 10, 29)

print(data_especifica)

#Acessando ano mês e dia

print(f'Ano: {hoje.year}')

print(f'Mês: {hoje.month}')

print(f'Dia: {hoje.day}')