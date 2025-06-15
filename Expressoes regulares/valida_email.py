import re

exemplo = "rlucas.rs@gmail.com"

def valida_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.search(padrao, email) is not None


email = 'lucas-renato@gmail.com'

print(valida_email(email))

