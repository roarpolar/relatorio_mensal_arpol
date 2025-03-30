import os
import requests
from dotenv import load_dotenv # type: ignore

def get_api_credentials():
    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()

    # URL da API do Zerosheet e Token
    api_url = os.getenv('API_URL')
    api_token = os.getenv('API_TOKEN')

    return api_url, api_token

def fetch_data(api_url=None, token=None):
    # Se não foram fornecidas credenciais, tenta obter do .env
    if not api_url or not token:
        api_url, token = get_api_credentials()

    # Verificar se as variáveis foram carregadas corretamente
    if not api_url or not token:
        print("Erro: Variáveis de ambiente não carregadas corretamente.")
        return None

    try:
        response = requests.get(api_url, headers={'Authorization': f'Bearer {token}'})
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Erro na requisição: {req_err}')
    except requests.exceptions.JSONDecodeError as json_err:
        print(f'Erro ao decodificar JSON: {json_err}')
    return None

if __name__ == "__main__":
    # Consumir dados da API apenas se executado diretamente
    data = fetch_data()
    
    if data:
        print("\nDados recebidos:")
        print(f"Tipo de dados: {type(data)}")
        print(f"Quantidade de registros: {len(data)}")
        
        if isinstance(data, list) and data:
            print("\nPrimeira linha de dados:")
            print(data[0])
    else:
        print('Nenhum dado encontrado.')