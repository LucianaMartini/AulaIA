# Atividade Prática 3 - Crie um script em Python 
# que leia um arquivo CSV e exiba os dados na tela. 
# O arquivo CSV deve conter informações de pessoas, 
# com colunas Nome, Idade e Cidade.

import csv 

dados = [["Nome", "Idade", "Cidade"], ["Ana", 28, "São Paulo"], ["Ribeiro", 25, "Rio de Janeiro"], ["Monteiro", 30, "Rio de Janeiro"]]

with open ("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)


with open ("dados.csv", mode="r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

    cabecalho = linhas[0].strip()

    nomes = []

    for linha in linhas [1:]:
        nomes.append(linha.strip())
    
print(cabecalho)
        
for nome in nomes:
    print(nome)