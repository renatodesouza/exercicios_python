class Endereco:
    def __init__(self, rua, numero, bairro, cep, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f'{self.rua}, {self.numero}, {self.bairro}, {self.cep}, {self.cidade}, {self.estado}'