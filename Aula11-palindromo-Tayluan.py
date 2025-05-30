def verifica_palindromo(palavra):
    palavra = palavra.lower()
    palavra_reverso = palavra[::-1]
    if palavra == palavra_reverso:
        print("SIM")
    else:
        print("NÃO")
verifica_palindromo("avo")
