import calendar
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

#Por padrão o primeiro dia da semana é segunda feira
#Podemos alterar isso

calendar.setfirstweekday(calendar.SUNDAY)

#Gerando um calendario mensal

print(calendar.month(202, 12))

#Exibindo o calendario anual

print(calendar.calendar(2024))

#Verificando se um ano é bissexto, se for bissexto retorna true se não retorna false
print(calendar.isleap(2023))

#Retorna o nuemro de anos bissextos em um intervalo
print(calendar.leapdays(2000, 2025))

#Retornando o dia da semana do primeiro dia do mês e a quantidade de dias do mês
print(f'Retornando o preimeiro dia do mes de janeiro de 2024: {calendar.monthrange(2024, 1)}')

#Retornando o dia da semana

print(calendar.weekday(2024, 12, 23))

#Retornando uma lista de semanas do mes, onde cada lista tem 7 dias os dias que não fazem parte do mes 
#são representados por 0, exemplo: [0, 0, 0, 1, 2, 3, 4]

print(calendar.monthcalendar(2024, 11))


#Iterando sobre os dias da semana
# for day in calendar.iterweekdays():
#     print(day)  # 0 = segunda, 1 = terça, ...

#verifica todas as sextas feiras 13 de um ano
year = 2011

for month in range(1, 13):
    if calendar.weekday(year, month , 13) == 4: # verifica se é igual a 4 por que a semana começa no 0 segunda feira 4 é a sexta feira
        print(f'Sexta feira 13 encontrada em {calendar.month_name[month]} {year}')

#verificando quantas vezes em um ano o dia 29 caiu em um domingo

year = 2024

for month in range(1, 13):
    if calendar.weekday(year, month, 29) == 0:
        print(f'O dia 29 foi encontrado nos meses {calendar.month_name[month]} {year}')
    else:
        print(f'O dia 29 não ocorreu em uma segunda feira no mes {calendar.month_name[month]}.')