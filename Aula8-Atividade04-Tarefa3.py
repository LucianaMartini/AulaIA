def verificar_senha_forte():
    """
    Verifica se uma senha é forte:
    - Pelo menos 8 caracteres.
    - Pelo menos um número.
    Continua pedindo a senha até que seja válida ou o usuário digite 'sair'.
    """
    print("--- Verificador de Senha Forte ---")
    print("Regras: Mínimo de 8 caracteres e pelo menos um número.")
    print("Digite 'sair' a qualquer momento para encerrar.")

    while True:
        senha = input("\nDigite sua senha: ")

        if senha.lower() == 'sair':
            print("Saindo do verificador de senha.")
            break

        # Regra 1: Pelo menos 8 caracteres
        if len(senha) < 8:
            print("Senha fraca: Deve ter pelo menos 8 caracteres.")
            continue

        # Regra 2: Pelo menos um número
        tem_numero = False
        for char in senha:
            if char.isdigit(): # Verifica se o caractere é um dígito
                tem_numero = True
                break
        
        if not tem_numero:
            print("Senha fraca: Deve conter pelo menos um número.")
            continue
        
        # Se chegou até aqui, a senha é forte
        print("Senha forte! Parabéns.")
        break

# Executa o verificador de senha
verificar_senha_forte()