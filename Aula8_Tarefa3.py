# Tarefa 3 -  Conversor de Temperatura
print("Tarefa 3 -  Conversor de Temperatura")


# Dados Originais
valor_original = float(input("Informe o valor a ser convertido: "))
print("Informe a escala do valor a ser convertido:")
print("C - Celsius")
print("F - Fahrenheit")
print("K - Kelvin")
escala_original = str(input("Opção escolhida (C/F/K): "))


# Dados Para Conversão
print("Informe a escala para a qual deseja converter:")
print("C - Celsius")
print("F - Fahrenheit")
print("K - Kelvin")
escala_convertida = str(input("Opção escolhida (C/F/K): "))


# Cálculo
# Convertendo para uma base comum (Celsius) primeiro, se necessário
if escala_original == "F":
    temperatura_celsius = (valor_original - 32) * 5/9
elif escala_original == "K":
    temperatura_celsius = valor_original - 273.15
else:  # Já é Celsius
    temperatura_celsius = valor_original

# Convertendo da base Celsius para a unidade de destino
if escala_convertida == "F":
    temperatura_convertida = (temperatura_celsius * 9/5) + 32
    simbolo_destino = "F"
elif escala_convertida == "K":
    temperatura_convertida = temperatura_celsius + 273.15
    simbolo_destino = "K"
else:  # Destino é Celsius
    temperatura_convertida = temperatura_celsius
    simbolo_destino = "C"


# Resultado Apresentado
print(f"{valor_original} {escala_original} = {temperatura_convertida} {escala_convertida}")