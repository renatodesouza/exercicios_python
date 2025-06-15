from estudante import Estudante

class Graduacao(Estudante):
    def __init__(self, *args, tcc: str, estagio: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.tcc = tcc
        self.estagio = estagio

    def apresentar_tcc(self):
        return f'TCC: {self.tcc}'
    
    def relatorio_estagio(self):
        return f'Relatorio estagio: {self.estagio}'
