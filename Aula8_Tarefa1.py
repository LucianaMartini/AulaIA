# Tarefa 1 - Classificador de Idade
print("Tarefa 1 - Classificador de Idade")

idade = int(input("Digite a idade: "))

# Análise
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")