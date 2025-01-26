from datetime import date, datetime, time, timedelta
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

#1 Crie um objeto date para sua data de nascimento e exiba o ano, mês e dia separadamente.
nascimento = date(1984, 1, 29)

print(nascimento)

print(f'Ano: {nascimento.year}\nMês: {nascimento.month}\nDia: {nascimento.day}')


#2 Mostre a data de hoje no formato YYYY-MM-DD.
data_atual = datetime.now()

print(data_atual.strftime("%Y-%m-%d"))


#3 Crie um objeto time para representar 08:15:30 e exiba os valores de horas, minutos e segundos.

hora = time(8, 15, 30)

print(hora)

print(hora.hour)

print(hora.minute)

print(hora.second)

#4 Gere o horário atual e formate-o no estilo HH:MM AM/PM.
hora_atual = datetime.now()

print(f'Exibindo a hora atual: {hora_atual.strftime("%H:%M:%S")}')

print(datetime.now().time())

#5 Crie um objeto datetime para 31 de dezembro de 2025 às 23:59:59 e exiba em formato legível.

data = datetime(2025, 12, 31, 23, 59, 59)

print(f'Data: {data.day} de {data.strftime("%B")} de {data.year} às : {data.strftime("%H:%M:%S")}')

#6 Converta a string "2023-05-15 10:00" para um objeto datetime.

data_string = "15/05/2023 10:00:00"

data_formatada = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")

print(data_formatada)

#7 Calcule quantos dias faltam para o próximo ano (use a data atual).
data_atual = datetime.now()

ano_novo = datetime(2025, 1, 1)

dias_faltantes = ano_novo - data_atual

print(f'Faltam {dias_faltantes.days} dias para o ano novo')

#8 Formate a data e hora atuais para exibir apenas o mês e o ano (ex.: Dezembro 2024).
data_atual = datetime.now()

print(f'Data atual: {data_atual.strftime("%B")} {data_atual.year}')

#9 Crie uma função que receba uma string no formato DD/MM/YYYY e retorne o nome do dia da semana.
def dia_da_semana(string):
    data_formatada = datetime.strptime(string, "%d/%m/%Y")

    dia_semana = data_formatada.strftime("%A")

    return dia_semana

data = '23/12/2024'

print(dia_da_semana(data))

#10 Escreva um programa que recebe uma data de entrada e calcula quantos dias se passaram desde essa data.

def dias_passados(data):
    data_atual = datetime.now()

    data_formatada = datetime.strptime(data, "%d/%m/%Y")

    diferenca = data_atual - data_formatada

    return diferenca.days

data = "11/10/2024"

print(dias_passados(data))