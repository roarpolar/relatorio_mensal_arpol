import os
import requests
from dotenv import load_dotenv # type: ignore

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# URL da API do Zerosheet e Token
API_URL = os.getenv('API_URL')
TOKEN = os.getenv('API_TOKEN')

# Verificar se as variáveis foram carregadas corretamente
if not API_URL or not TOKEN:
    print("Erro: Variáveis de ambiente não carregadas corretamente.")
    exit(1)

def fetch_data(api_url, token):
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

# Consumir dados da API
data = fetch_data(API_URL, TOKEN)

if data:
    for row in data:
        print(row)
else:
    print('Nenhum dado encontrado.')