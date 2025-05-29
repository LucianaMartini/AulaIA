def classificar_impar_par():
    while True:            
        try:
            numero = input("Digite um número inteiro, ou digite 'fim' para encerrar.")
            if numero.lower() == "fim":
                break
            else:
                numero = int(numero)
                if numero % 2 == 0:
                    return " O número é PAR"
                else:
                    return " O número é IMPAR"
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 'fim' para encerrar.")
print(classificar_impar_par())