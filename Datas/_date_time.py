#Combinando data e hora com o objeto datetime

from datetime import datetime

agora = datetime.now()

print(agora)

#Criando data e hora especificas

data_hora_especifica = datetime(2024, 10, 11, 10, 50, 20)

print(data_hora_especifica)

#Acessando partes especificas ano, mes, dia, hora, minuto, segundo

print(f'Ano: {agora.year}\nMes: {agora.month}\nDia: {agora.day}\nHora: {agora.hour}\nMinuto: {agora.minute}\nSegundo: {agora.second}')