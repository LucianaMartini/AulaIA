def verificador_par_impar():
    """
    Solicita números inteiros ao usuário, informa se são pares ou ímpares,
    trata entradas inválidas e, ao final, mostra a contagem total.
    """
    print("--- Verificador de Números Pares e Ímpares ---")
    print("Digite números inteiros, ou 'fim' para encerrar.")

    total_pares = 0
    total_impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim'): ").strip().lower()

        if entrada == 'fim':
            print("\nEncerrando o programa.")
            break

        try:
            numero = int(entrada) # Tenta converter a entrada para um número inteiro
            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                total_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                total_impares += 1
        except ValueError:
            print(f"Erro: '{entrada}' não é um número inteiro válido. Por favor, digite um número inteiro.")
            continue # Continua para a próxima iteração do loop

    print("\n--- Resumo ---")
    print(f"Total de números PARES inseridos: {total_pares}")
    print(f"Total de números ÍMPARES inseridos: {total_impares}")

# Executa o verificador
verificador_par_impar()