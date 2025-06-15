# 6. Exercícios de Regex
# Exercício 1: Encontrar Palavras que Começam com Vogal
# Dado um texto, use regex para encontrar todas as palavras que começam com uma vogal 
# (a, e, i, o, u, independentemente de maiúsculas ou minúsculas).

# Dica: Utilize o padrão \b[aeiouAEIOU]\w*.

import re

texto = "!Dado !um texto, ?use regex para .encontrar todas as palavras que começam com uma vogal "

#\b é uma posicao e nao um caracter

padrao = r"\b[aeiouAEIOU]\w*"

resultado = re.findall(padrao, texto)

if resultado:
    print(resultado)


texto_dois = "# 6. Exercícios de Regex\
# Exercício 1: Encontrar Palavras que Começam com Vogal\
# Dado um texto, use regex para encontrar todas as palavras que começam com uma vogal \
# (a, e, i, o, u, independentemente de maiúsculas ou minúsculas)."


resultado = re.findall(padrao, texto_dois)

if resultado:
    print(resultado)


#Exercício 1: Encontrar Palavras que Terminam com uma Vogal
# Descrição:
# Dado um texto, encontre todas as palavras que terminam com uma vogal 
# (a, e, i, o, u — maiúsculas ou minúsculas).

# Dica:
# Utilize o metacaractere \b para indicar a fronteira da palavra e um padrão 
# que garanta que o último caractere seja uma vogal.

texto = "# Utilize o metacaractere \b para indicar a fronteira da palavra e um padrão \
# que garanta que o último caractere seja uma vogal."

padrao = r'\b\w*[aeiouAEIOU]\b'

resultado = re.findall(padrao, texto)

if resultado:
    print(resultado)