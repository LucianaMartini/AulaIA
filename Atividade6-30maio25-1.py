import random

def gerar_senha_simples():
    print("Gerador de senhas aleatórias simples")
    tamanho_senha = int(input("Digite o número de caracteres que a senha deverá ter: "))

    caracteres_disponiveis = "abcdefghijklmnopqrstuvwxyz" \
                           + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                           + "0123456789" \
                           + "!@#$%^&*()_+-=[]{}|;:,.<>/?~"
    
    senha_gerada = ""
    for _ in range(tamanho_senha):
        caractere_aleatorio = random.choice(caracteres_disponiveis)
        senha_gerada += caractere_aleatorio

    print(f"\nSua senha aleatória é: {senha_gerada}")

if __name__ == "__main__":
    gerar_senha_simples()