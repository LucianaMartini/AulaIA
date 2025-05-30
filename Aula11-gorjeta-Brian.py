def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta *(porcentagem_gorjeta /100)
    return round(gorjeta, 2)

total_conta = 100.00
porcentagem = 15
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R$ {total_conta:.2f}, a gorjeta de {porcentagem}% é de R$ {gorjeta}.")
