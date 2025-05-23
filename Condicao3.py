# Tarefa 4 - Análise de Números 
print("Tarefa 4 - Análise de Números")

num = int(input("Digite o número: "))

# Positivo ou Negativo
if num > 0 and num % 2 == 0:
    print("Positivo e Par")
elif num > 0 and num % 2 != 0:
    print("Positivo e Ímpar")
elif num < 0 and num % 2 == 0:
    print("Negativo e Par")
elif num < 0 and num % 2 != 0:
    print("Negativo e Impar")  
else:
    print("Número igual a zero")