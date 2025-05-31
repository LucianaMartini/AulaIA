import requests

def gerar_perfil_aleatorio():
    print("Gerador de Perfil de Usuário Aleatório")

    url_api = "https://randomuser.me/api/"

    try:
        print("Buscando dados de um novo usuário...")
        resposta = requests.get(url_api)
        resposta.raise_for_status()
        dados = resposta.json()
        usuario = dados['results'][0]

        nome_titulo = usuario['name']['title']
        nome_primeiro = usuario['name']['first']
        nome_sobrenome = usuario['name']['last']
        email = usuario['email']
        pais = usuario['location']['country']

        # Resultado exibido
        print("\nPerfil Gerado")
        print(f"Nome: {nome_titulo}. {nome_primeiro} {nome_sobrenome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    finally:
        print("Consulta finalizada.")

if __name__ == "__main__":
    gerar_perfil_aleatorio()