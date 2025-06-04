# Atividade Prática 4 - Crie um script em Python 
# que leia e escreva dados em um arquivo JSON. 
# O arquivo JSON deve conter informações de uma 
# pessoa, com campos nome, idade e cidade.​

import json

dados = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "São Paulo"
}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)