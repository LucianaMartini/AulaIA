import requests

def consultar_cotacao_moeda():
    print("\nConversão de Moedas para Real Brasileiro 'BRL'")

    while True:
        codigo_moeda = input("Digite o código da moeda (ex: USD, EUR) ou 'sair' para encerrar: ").strip().upper()

        if codigo_moeda == 'SAIR':
            print("Saindo do programa.")
            break

        url_api = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"

        try:
            print(f"Buscando cotação para {codigo_moeda}/BRL...")
            resposta = requests.get(url_api)
            resposta.raise_for_status()
            dados_cotacao = resposta.json()

            if not dados_cotacao or f"{codigo_moeda}BRL" not in dados_cotacao:
                print(f"Não foi possível encontrar a cotação para '{codigo_moeda}'. Verifique o código da moeda ou tente outra.")
                continue
            
            cotacao = dados_cotacao[f"{codigo_moeda}BRL"]
            
            # Informações desejadas
            valor_compra = float(cotacao.get('bid', 0.0))
            valor_venda = float(cotacao.get('ask', 0.0))
            valor_maximo = float(cotacao.get('high', 0.0))
            valor_minimo = float(cotacao.get('low', 0.0))
            
            # A data e hora da última atualização
            data_atualizacao = cotacao.get('create_date', 'Data/Hora não disponível')

            # Exibe as informações formatadas
            print(f"\nCotação de {codigo_moeda}/BRL")
            print(f"Valor de Compra (BID):     R$ {valor_compra:.4f}")
            print(f"Valor de Venda (ASK):      R$ {valor_venda:.4f}")
            print(f"Valor Máximo (24h):        R$ {valor_maximo:.4f}")
            print(f"Valor Mínimo (24h):        R$ {valor_minimo:.4f}")
            print(f"Última Atualização:        {data_atualizacao}")
            print("------------------------------------------\n")
        except:
            print("Moeda inválida, digite o código correto.")
            
if __name__ == "__main__":
    consultar_cotacao_moeda()