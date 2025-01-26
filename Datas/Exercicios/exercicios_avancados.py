from datetime import datetime, timedelta

# Calcule a idade de uma pessoa:

# Peça a data de nascimento do usuário no formato DD/MM/YYYY e calcule a idade atual.

data = input("Informe sua data de nascimento no formato dd/mm/aaaa: ")

data_formatada = datetime.strptime(data, "%d/%m/%Y")

data_final = data_formatada.strftime("%d/%m/%Y")

data_atual = datetime.now()

idade = data_atual.year - data_formatada.year

print(idade)