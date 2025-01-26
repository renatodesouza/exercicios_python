#Use map() para gerar siglas com as primeiras letras de cada palavra.

estados = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia", "Paraná"]

novo = [cidade.split() for cidade in estados]

print(novo)