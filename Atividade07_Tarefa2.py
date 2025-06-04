# Atividade Prática 2 - Crie um script em Python 
# que escreva dados em um arquivo CSV. O arquivo CSV 
# deve conter informações de pessoas, 
# com colunas Nome, Idade e Cidade.​

import csv

def escrever_csv(nome_arquivo, dados):
    
    colunas = ["nome", "idade", "cidade"]
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")

dados_pessoas = [
    {"nome": "Luciana", "idade": 30, "cidade": "São Bernardo do Campo"},
    {"nome": "Tayluan", "idade": 20, "cidade": "São João de Meriti"},
    {"nome": "Priscila", "idade": 26, "cidade": "Pernambuco"}
]

escrever_csv("pessoas.csv", dados_pessoas)