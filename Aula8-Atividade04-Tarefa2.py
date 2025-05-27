def registrar_notas_turma():
    """
    Permite ao professor registrar notas de 0 a 10 para a turma.
    Ignora notas inválidas, e ao final, calcula e exibe a média da turma.
    """
    print("--- Registro de Notas da Turma ---")
    print("Digite as notas (entre 0 e 10). Digite 'fim' para encerrar.")

    notas = []
    total_notas_validas = 0
    soma_das_notas = 0.0

    while True:
        entrada = input("Digite a nota (ou 'fim'): ").strip().lower()

        if entrada == 'fim':
            print("\nEncerrando o registro de notas.")
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
                soma_das_notas += nota
                total_notas_validas += 1
                print(f"Nota {nota:.1f} registrada.")
            else:
                print("Nota inválida: A nota deve estar entre 0 e 10. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida: Por favor, digite um número para a nota ou 'fim'.")
            continue # Continua para a próxima iteração do loop

    print("\n--- Resumo do Registro ---")
    if total_notas_validas > 0:
        media_turma = soma_das_notas / total_notas_validas
        print(f"Número total de notas válidas inseridas: {total_notas_validas}")
        print(f"Média da turma: {media_turma:.2f}")
    else:
        print("Nenhuma nota válida foi inserida para calcular a média.")

# Executa o programa de registro de notas
registrar_notas_turma()