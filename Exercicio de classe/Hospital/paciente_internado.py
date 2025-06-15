from paciente import Paciente
from datetime import date

class PacienteInternado(Paciente):
    def __init__(self, *args, data_internacao: date, num_leito, 
                 plano_saude, procedimentos_realizados, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_internacao = data_internacao
        self.num_leito = num_leito
        self.plano_saude = plano_saude
        self.procedimentos_realizados = procedimentos_realizados

        