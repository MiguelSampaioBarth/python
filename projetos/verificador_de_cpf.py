import os

def valida_cpf(cpf):
    os.system('cls' if os.name == 'nt' else 'clear')

    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    peso = 10
    for digit in cpf[:9]:
        soma += int(digit) * peso
        peso -= 1

    resto = 11 - (soma % 11)
    digito1 = resto if resto < 10 else 0

    # Calcula o segundo dígito verificador
    soma = 0
    peso = 11
    for digit in cpf[:10]:
        soma += int(digit) * peso
        peso -= 1

    resto = 11 - (soma % 11)
    digito2 = resto if resto < 10 else 0

    # Verifica se os dígitos calculados coincidem com os informados
    return cpf[-2:] == f'{digito1}{digito2}'

while True :
    cpf_digitado = input('insira seu CPF:\n')

    if valida_cpf(cpf_digitado):
        print("Seu CPF é válido")
        
    else:
        print("O CPF inserido não é válido")
        continue
