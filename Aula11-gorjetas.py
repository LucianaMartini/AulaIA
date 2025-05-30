# Cálculo de Gorjeta
# Calcula o valor da gorjeta baseada no valor total da conta e na porcentagem de gorjeta desejada.​

def calcular_gorjeta():
    print("Calculadora de Gorjetas")

    # Valor da Conta
    while True:
        try:
            valor_conta_str = input("Digite o valor total da conta: R$ ")
            valor_conta = float(valor_conta_str)
            if valor_conta < 0:
                print("O valor não pode ser negativo. Digite um número válido.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite o valor correto.")

    # Porcentagem da gorjeta:
    while True:
        try:
            percentual_gorjeta_str = input("Digite a porcentagem da gorjeta (%): ")
            percentual_gorjeta = float(percentual_gorjeta_str)
            if percentual_gorjeta < 0:
                print("A porcentagem de gorjeta não pode ser negativa. Digite um número válido.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite a porcentagem correta.")

    # Cálculo do valor da gorjeta
    valor_gorjeta = valor_conta * (percentual_gorjeta / 100)

    # Cálculo do total a pagar
    total_a_pagar = valor_conta + valor_gorjeta

    # Resultado informado
    print(f"\nDETALHES DA CONTA")
    print(F"Valor da conta: R$ {valor_conta:.2f}")
    print(F"Porcentagem da gorjeta: {percentual_gorjeta:.0f} %")
    print(F"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    print(F"Total a pagar: R$ {total_a_pagar:.2f}")

calcular_gorjeta()