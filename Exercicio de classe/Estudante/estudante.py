from datetime import date
from endereco import Endereco

class Estudante:
    def __init__(self, nome, email, telefone, endereco: Endereco, data_nasc: date, sexo: str, cpf: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.cpf = cpf

    def validar_cpf(self):
        nums = [int(d) for d in self.cpf if d.isdigit()]
        return len(nums)
    
    def idade(self):
        hoje = date.today()
        anos = hoje.year - self.data_nasc.year

        if (hoje.month, hoje.day) < (self.data_nasc.month, self.data_nasc.day):
            anos -= 1
            return anos
        
    def resumo(self):
        return f'Nome: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}\nEndereco: {self.endereco}\nData de Nasc: {self.data_nasc}\nSexo: {self.sexo}\nCPF: {'Valido' if self.validar_cpf() else 'Inválido'}'