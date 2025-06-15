import re

texto = "Meu email é rlucas@gmail.com"

padrao = r"(\w+)@(\w+\.\w+)"

resultado = re.search(padrao, texto)

if resultado:
    print(f'Usuario {resultado.group(1)}')
    print(f'Dominio {resultado.group(2)}')
    

#Para usar caracters especiais como parte do texto use a \ invertida

texto = "O preço é R$ 100"

resultado = re.search("R\$\s?\d+", texto)

if resultado:
    print(f"O padrao foi encontrado: {resultado.group()}")