from datetime import datetime



#O strptime converte datas em strings para objetos datetime

data_string = "15/12/24 15:30:20"

data_convertida = datetime.strptime(data_string, "%d/%m/%y %H:%M:%S")

print(data_convertida)


