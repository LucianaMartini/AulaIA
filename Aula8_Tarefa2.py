# Tarefa 2 -  Calculadora de IMC
print("Tarefa 2 - Calculadora de IMC")


# Dados Solicitados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))


# IMC Calculado
imc = peso / (altura ** 2)
print(f"seu IMC (kg/m²) é {imc:.2f}")


# Análise
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")