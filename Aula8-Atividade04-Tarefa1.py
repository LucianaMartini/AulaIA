def calculadora():
    """
    Uma calculadora que realiza as quatro operações básicas entre dois números.
    Trata erros de entrada não numérica, divisão por zero e operação inválida.
    Repete até uma operação válida ser concluída.
    """
    print("--- Calculadora Simples ---")
    print("Esta calculadora realiza as operações de adição (+), subtração (-), multiplicação (*) e divisão (/).")

    while True:
        try:
            # Solicita o primeiro número
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str) # Tenta converter para float

            # Solicita a operação
            operacao = input("Digite a operação (+, -, *, /): ").strip()

            # Solicita o segundo número
            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str) # Tenta converter para float

            resultado = None

            # Realiza a operação com base na escolha do usuário
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero não é permitida. Por favor, tente novamente.")
                    continue # Volta para o início do loop
            else:
                print("Erro: Operação inválida. Por favor, use +, -, * ou /.")
                continue # Volta para o início do loop

            # Se chegamos aqui, a operação foi válida e o resultado foi calculado
            print(f"\nResultado: {num1} {operacao} {num2} = {resultado:.2f}")
            break # Sai do loop principal pois uma operação válida foi concluída

        except ValueError:
            # Captura erro se a entrada do número não for numérica
            print("Erro: Entrada inválida. Por favor, digite apenas números válidos para os operandos.")
            # O 'continue' implícito aqui fará com que o loop se repita
        except Exception as e:
            # Captura qualquer outro erro inesperado
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")
            # O 'continue' implícito aqui fará com que o loop se repita

# Chama a função da calculadora para iniciar o programa
calculadora()