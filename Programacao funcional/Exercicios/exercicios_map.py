# 1️⃣ Dada a lista nomes = ["alice", "bob", "carlos"], use map() para transformar todos os nomes em letras maiúsculas.

nomes = ["alice", "bob", "carlos"]

print(list(map(lambda nome: nome.upper(), nomes)))


# 2️⃣ Dada a lista numeros = [2, 4, 6, 8], use map() para calcular o quadrado de cada número.

numeros = [2, 4, 6, 8]

numero_quadrado = list(map(lambda x: x ** 2, numeros))

print(numero_quadrado)

# 3️⃣ Dada a lista palavras = ["Python", "é", "incrível"], use map() para calcular o comprimento de cada palavra.

palavras = ["Python", "é", "incrível"]

comprimento = list(map(len, palavras))

print(comprimento)


# 4️⃣ Dada a lista temperaturas_celsius = [0, 20, 30, 40], use map() para converter as temperaturas para Fahrenheit. (Fórmula: F = C * 9/5 + 32)

temperaturas_celsius = [0, 20, 30, 40]

fahrenheit = list(map(lambda c: c * (9 / 5) + 32, temperaturas_celsius))

print(fahrenheit)

# 5️⃣ Dada a lista precos = [10, 20, 30], aplique um desconto de 10% usando map().

precos = [10, 20, 30, 4500]

preco_com_desconto = list(map(lambda x: x - (10 * x) / 100, precos))

print('5---', preco_com_desconto)

# 6️⃣ Dada a lista palavras = ["Python", "é", "fantástico"], use map() para reverter cada palavra.

palavras = ["Python", "é", "fantástico"]

print(list(map(lambda x: x[::-1], palavras)))

# 7️⃣ Dada a lista distancias_km = [5, 10, 15], converta para milhas (1 km = 0.621371 milhas).

distancias_km = [5, 10, 15]

milhas = list(map(lambda x: x * 0.621371, distancias_km))

milhas_arredondadas = [round(x, 2) for x in milhas]

print(milhas_arredondadas)

# 8️⃣ Dada a lista numeros = [1, 2, 3, 4], transforme cada número em uma string usando map().

numeros = [1, 2, 3, 4]

strings = list(map(str, numeros))

print(strings)

# 9️⃣ Dada a lista valores = [100, 200, 300], aplique um imposto de 15% sobre cada valor.

valores = [100, 200, 300]

valor_com_imposto = list(map(lambda x: (x * 0.15) + x, valores))

print(valor_com_imposto)

# 🔟 Dada a lista frases = ["Ola mundo", "Python é ótimo", "Aprendendo programação"], use map() para contar quantas palavras há em cada frase.

frases = ["Ola mundo", "Python é ótimo", "Aprendendo programação"]

print(list(map(lambda x: len(x.split()), frases)))