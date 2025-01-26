from collections import namedtuple

estados = namedtuple('Estados', ['sigla', 'nome'])

Sao_Paulo = estados('SP', 'São Paulo')

print(Sao_Paulo)

print(Sao_Paulo.sigla)

print(Sao_Paulo.nome)

print(type(Sao_Paulo.sigla))