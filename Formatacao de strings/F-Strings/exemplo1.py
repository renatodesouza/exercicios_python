nascimento = 1984

data_atual = 2024

print(f'Minha idade é {data_atual - nascimento}')

#Alinhamento
# - < à esquerda
# - > à direita
# - ^ centralizado

texto = 'python'

print(f'À esquerda: |{texto:<10}|')
print(f'À direita: |{texto:>10}|')
print(f'Centralizado: |{texto:^10}|')

#Definindo o preenchimento
print(f'À esquerda: |{texto:010}|')

lista = ['renato', 40]


print(f'meu nome {lista[0]} minha idade {lista[1]}')
