from estudante import Estudante


class PosGraduacao(Estudante):
    def __init__(self, *args, artigo: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.artigo = artigo

    
    def apresentar_artigo(self):
        return f'Apresentação artigo {self.artigo}'