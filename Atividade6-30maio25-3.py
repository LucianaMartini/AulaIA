import requests # Precisamos deste módulo para fazer a requisição à internet

def consultar_cep_viacep():
    
    print("Consulta de CEP - ViaCEP")

    while True:
        cep = input("Digite o CEP (apenas números, ex: 01001000) ou 'sair' para encerrar: ").strip()

        if cep.lower() == 'sair':
            print("Saindo do programa.")
            break

        if not (cep.isdigit() and len(cep) == 8):
            print("CEP inválido. Digite 8 números ou 'sair'.")
            continue

        url_api = f"https://viacep.com.br/ws/{cep}/json/"

        try:
            print(f"Buscando informações para o CEP: {cep}...")
            resposta = requests.get(url_api)

            resposta.raise_for_status()

            dados_endereco = resposta.json()

            if 'erro' in dados_endereco and dados_endereco['erro'] == True:
                print(f"CEP '{cep}' não encontrado ou inválido. Por favor, verifique.")
            else:
                logradouro = dados_endereco.get('logradouro', 'Não informado')
                bairro = dados_endereco.get('bairro', 'Não informado')
                cidade = dados_endereco.get('localidade', 'Não informado')
                estado = dados_endereco.get('uf', 'Não informado')

                # Resultado exibido
                print("\nEndereço Encontrado")
                print(f"CEP: {cep}")
                print(f"Logradouro: {logradouro}")
                print(f"Bairro: {bairro}")
                print(f"Cidade: {cidade}")
                print(f"Estado: {estado}")
                print("---------------------------\n")

        finally:
            print("\nSe você recebeu resultados corretos, parabéns!")
            print("\nCaso o resultado exibido seja insatisfatório")
            print("é porque você digiou parâmetros inválidos.")
            print("Seja mais cuidadoso da próxima vez. Boa sorte!")
            print("\nDigite um novo CEP ou 'sair' para encerrar a consulta.")

if __name__ == "__main__":
    consultar_cep_viacep()