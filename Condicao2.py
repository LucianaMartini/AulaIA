# Tarefa 3 - Calculadora de Idade
print("Tarefa 3 - Calculadora de Idade")

idade = int(input("Digite a idade: "))

# Análise
if idade < 13:
    print("Criança")
elif idade < 20:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")