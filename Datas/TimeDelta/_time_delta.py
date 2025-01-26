from datetime import datetime , timedelta


#O objeto timedelta do módulo datetime representa uma duração de tempo
#Utilizamos ele para realizar operações de adição e subtração em objetos date ou datetime

data_atual = datetime.now()

intervalo = timedelta(days=7)

nova_data = data_atual + intervalo

print(data_atual)

print(nova_data)

#Diferença entre dois objetos date ou datetime retorna um objeto timedelta, que contém a duração entre eles
#Atributos days, seconds e total_seconds

data1 = datetime(2024, 12, 1)

data2 = datetime(2024, 12, 25)

diferenca = data1 - data2

print(f'Diferença de dias: {diferenca.days}')

print(f'Diferença em segundos: {diferenca.total_seconds()}')

print(type(diferenca))

#Exemplo com data atual

data_atual = datetime.now()

aniversario = datetime(2025, 1, 29)

diferenca = data_atual - aniversario

print(f'Total de dias que faltam para meu aniversario: {diferenca.days}')