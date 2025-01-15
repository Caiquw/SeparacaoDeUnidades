nome = str(input("Insira seu nome completo\n")).strip()
nomespl= nome.split()

print(f"Nome em caixa-alta: {nome.upper()}")
print(f"Nome em caixa-baixa: {nome.lower()}")
print(f"Número de letras no nome: {len(nome) - nome.count(' ')}")
print(f"Número de letras do primeiro nome: {len(nomespl[0])}")
