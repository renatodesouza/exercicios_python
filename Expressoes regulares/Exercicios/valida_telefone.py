import re

fone = '(11)99827-4247 (11)22547-8956'

padrao = r'\(\d{2}\)\s?\d{4,5}-\d{4}'

resultado = re.findall(padrao, fone)

if resultado:
    print(resultado)