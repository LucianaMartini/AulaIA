# Tarefa 4 -  Verificador de Ano Bissexto
print("Tarefa 4 -  Verificador de Ano Bissexto")

# Ano Verificado
ano = int(input("Digite um ano: "))

# Análise
if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")