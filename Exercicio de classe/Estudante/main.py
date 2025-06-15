from estudante import Estudante
from endereco import Endereco
from graduacao import Graduacao
from pos_graduacao import PosGraduacao
from datetime import date


if __name__ == "__main__":
    end = Endereco("Av. Brasil", 100, "Centro", "01000-000", "São Paulo", "SP")
    grad = Graduacao(
        nome="Ana Silva",
        email="ana.silva@email.com",
        telefone="(11)99999-0000",
        endereco=end,
        data_nasc=date(2002, 5, 20),
        sexo="F",
        cpf="123.456.789-09",
        tcc="Desenvolvimento de APIs em Python",
        estagio="Tech Solutions"
    )
    print("--- Cadastro Graduação ---")
    print(grad.resumo())
    print(grad.apresentar_tcc())
    print(grad.relatorio_estagio())

    pos = PosGraduacao(
        nome="Bruno Costa",
        email="bruno.costa@email.com",
        telefone="(21)98888-1111",
        endereco=end,
        data_nasc=date(1995, 8, 15),
        sexo="M",
        cpf="987.654.321-00",
        artigo="Machine Learning em Processamento de Imagens"
    )
    print("\n--- Cadastro Pós‑Graduação ---")
    print(pos.resumo())
    print(pos.apresentar_artigo())
