def verificar_palindromo_interativo():

    print("--- Verificador de Palíndromos ---")
    texto_original = input("Digite uma palavra ou frase para verificar: ")

    # 1. Converter para minúsculas para ignorar case
    texto_processado = texto_original.lower()

    # 2. Remover caracteres não alfanuméricos (espaços, pontuação, etc.)
    # Vamos construir uma nova string apenas com letras e números
    texto_limpo = ""
    for caractere in texto_processado:
        if ('a' <= caractere <= 'z') or ('0' <= caractere <= '9'):
            texto_limpo += caractere

    # 3. Comparar a string limpa com sua versão invertida
    # [::-1] é um "slice" que inverte a string
    texto_invertido = texto_limpo[::-1]

    if texto_limpo == texto_invertido:
        print(f"'{texto_original}' é um palíndromo? Sim")
    else:
        print(f"'{texto_original}' é um palíndromo? Não")

# --- Para rodar o verificador ---
if __name__ == "__main__":
    verificar_palindromo_interativo()