numero = int(input("digite o número: "))

if numero == 0:
    print("O número é igual a zero")
elif numero > 0:
    print("O número é maior que zero")
else:
    print("O número é menor que zero")




# Tarefa 3 - Calculadora de Média Escolar
print("Tarefa 3 - Calculadora de Média Escolar")

# Notas
nota1 = 5
nota2 = 5
nota3 = 5

# Cálculo da média
somaT = nota1 + nota2 + nota3
media = somaT / 3

# Resultado exibido
print("As notas consideradas neste cálculo são: ")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"A média calculada é: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")



