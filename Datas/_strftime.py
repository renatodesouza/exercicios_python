#Formatando datas e horarios como strings personalizadas utilizando o strftime

from datetime import datetime

agora = datetime.now()


print(f'Exibindo somente a data atual, dia, mes, ano, hora, minuto e segundo:\n {agora}')

data = agora.strftime(f'Exibindo a data formatada dia, mês e ano: {"%d/%m/%y"}')

print(data)

ano_quatro_digitos = agora.strftime(f'Exibindo a data com o ano com quatro digitos: {"%d/%m/%Y"}')

print(ano_quatro_digitos)

hora = agora.strftime(f'Exibindo a hora formatada hora, minuto e segundo: {"%H:%M:%S"}')

print(hora)

#Data curta dia, mes e ano
print('Data curta: ', agora.strftime("%d/%m/%y"))

#Mes por extenso
print("Mês por extenso, ", agora.strftime("%B"))

print("Dia da semana: ", agora.strftime("%A"))