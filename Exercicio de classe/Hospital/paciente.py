from datetime import date
from ..Estudante.endereco import Endereco


class Paciente:
    def __init__(self, nome, email, telefone, endereco: Endereco,
                 data_nasc: date, sexo, cpf, peso: float, altura: float, alergias):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.cpf = cpf
        self.peso = peso
        self.altura = altura
        self.alergias = alergias

    def __str__(self):
        return f'{self.nome}\n{self.email}\n{self.telefone}\n{self.endereco}\
            {self.data_nasc}\n{self.sexo}\n{self.cpf}\n{self.peso}\n{self.altura}\n{self.alergias}'

