from datetime import datetime


#Removendo microsegundos de um datetime.now().time()
hora_atual = datetime.now().time()

print(f'Hora com microsegundos: {hora_atual}')

#Hora sem microsegundos

hora_sem_microsegundos = hora_atual.replace(microsecond=0)

print(f'Hora sem microsegundos: {hora_sem_microsegundos}')

#-----------Removendo segundos------------------------
hora_sem_segundos = hora_atual.replace(second=0, microsecond=0)

print(f'Zerando os segundos: {hora_sem_segundos}')

