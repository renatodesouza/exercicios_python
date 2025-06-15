import re

texto = 'A data de hoje é 02/02/2025'

# novo_texto = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", texto)

novo_texto = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", texto)

print(novo_texto)


