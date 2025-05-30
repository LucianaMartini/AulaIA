def calculo_idade(ano_nascimento, ano_atual):
    total_dias = (ano_atual - ano_nascimento) * 365
    return total_dias
resultado = calculo_idade(1998, 2025)
print(f"Você tem {resultado} dias de vida.")