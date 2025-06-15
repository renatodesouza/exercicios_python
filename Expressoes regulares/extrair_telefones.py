import re


texto = "Ligue para o numero (11)2017-8596 ou 2016-8525\
    outras regioes fora de sao paulo (11)-2541-2325"

telefones = re.findall(r"\d{4}-\d{4}", texto)

print(telefones)

