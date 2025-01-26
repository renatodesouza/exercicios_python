#1️⃣ Corrigir capitalização de nomes
# Dada a lista nomes = ["joão silva", "maria oliveira", "carlos almeida"], 
# use map() para garantir que cada palavra do nome comece com letra maiúscula.

nomes = ["joão silva", "maria oliveira", "carlos almeida"]

print(list(map(lambda nome: nome.upper(), nomes)))

# 2️⃣ Remover espaços extras em uma lista de frases
# Dada a lista frases = [" Olá mundo ", " Python é incrível ", " Aprendendo programação "], 
# use map() para remover os espaços extras de cada frase.

frases = [" Olá mundo ", " Python é incrível ", " Aprendendo programação "] 

print(list(map(lambda nome: nome.strip(), frases)))

#3️⃣ Corrigir um cálculo de percentual
# Dada a lista precos = [100, 250, 400], use map() para calcular o valor final após um desconto de 20%.

precos = [100, 250, 400]

print(list(map(lambda preco: preco - (preco * 0.20)/ 100, precos)))

#4️⃣ Converter todas as palavras para minúsculas
# Dada a lista palavras = ["Python", "Linguagem", "PROGRAMAÇÃO"], 
# use map() para converter todas as palavras para letras minúsculas.

palavras = ["Python", "Linguagem", "PROGRAMAÇÃO"]

print(list(map(lambda palavra: palavra.lower(), palavras)))

# 5️⃣ Contar palavras corretamente
# Dada a lista frases = ["Python é bom", "Estou aprendendo programação", "Funções são úteis"], use map() para contar quantas palavras há em cada frase.

frases = ["Python é bom", "Estou aprendendo programação", "Funções são úteis"]

print(list(map(lambda palavra: len(palavra.split()), frases)))

#6️⃣ Converter temperaturas de Fahrenheit para Celsius
# Dada a lista temperaturas_fahrenheit = [32, 68, 100], use map() para convertê-las para Celsius.
# C = (F - 32) x 5 / 9

temperaturas_fahrenheit = [32, 68, 100]

print(list(map(lambda f: (f - 32) * 5 / 9, temperaturas_fahrenheit)))

#7️⃣ Calcular a raiz quadrada de uma lista de números
# Dada a lista numeros = [4, 9, 16, 25], use map() para calcular a raiz quadrada de cada número.

# 📌 Dica: O operador ** ou a função math.sqrt() podem ajudar.
from math import sqrt
numeros = [4, 9, 16, 25]

print(list(map(sqrt, numeros)))

#8️⃣ Formatar números de uma lista como strings
#Dada a lista numeros = [3.14159, 2.71828, 1.61803], use map() para formatá-los com apenas 2 casas decimais.

#📌 Dica: A função round() pode ser útil.

numeros = [3.14159, 2.71828, 1.61803]

print(list(map(lambda x: round(x, 2), numeros)))

#9️⃣ Criar siglas a partir de frases
# Dada a lista frases = ["Python é incrível", "Desenvolvimento Web", "Programação Funcional"], use map() para transformar cada frase em uma sigla.

# 📌 Exemplo: "Python é incrível" → "PEI"

nome = 'python é incrivel'

print(nome.split(' '))

frases = ["Python é incrível", "Desenvolvimento Web", "Programação Funcional"]

print([palavra[0] for palavra in frases])

siglas = list(map(lambda frase: "".join([palavra[0].upper() for palavra in frase.split()]), frases))

print(siglas)

lista = ['brasil', 'argentina', 'alemanha', 'portugal', 'bolivia', 'italia']

siglas_paises = list(map(lambda pais: pais[:2].upper(), lista))

print(siglas_paises)