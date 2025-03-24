import requests  # Importa a biblioteca requests para realizar requisições HTTP

# URL da API do Zerosheet - onde os dados serão buscados
API_URL = 'https://api.zerosheets.com/v1/wv8c'

# Token de autorização para acessar a API 
TOKEN = 'LNNCoCVgZOxwefUwt5stfbn77bi0LlD6'

# Função para buscar dados da API
def fetch_data(api_url, token):
    try:
        # Realiza uma requisição GET na API, passando o token no cabeçalho para autorização
        response = requests.get(api_url, headers={'Authorization': f'Bearer {token}'})
        
        # Verifica se a resposta da API teve algum erro (status code diferente de 200)
        response.raise_for_status()
        
        # Tenta converter a resposta para JSON
        data = response.json()
        return data

    # Trata erros de HTTP (ex.: 404, 500)
    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
    
    # Trata erros relacionados à requisição, como falha de conexão
    except requests.exceptions.RequestException as req_err:
        print(f'Erro na requisição: {req_err}')
    
    # Trata erros ao tentar decodificar o JSON (caso a resposta não seja um JSON válido)
    except requests.exceptions.JSONDecodeError as json_err:
        print(f'Erro ao decodificar JSON: {json_err}')
    
    # Retorna None se houver algum erro na requisição ou conversão
    return None

# Consome os dados da API chamando a função fetch_data
data = fetch_data(API_URL, TOKEN)

# Verifica se algum dado foi retornado e, se sim, exibe linha por linha
if data:
    for row in data:
        print(row)  # Exibe cada linha de dados retornada pela API
else:
    print('Nenhum dado encontrado.')  # Mensagem exibida caso não haja dados disponíveis