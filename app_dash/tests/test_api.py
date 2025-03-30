import pytest
from api.relatorio import fetch_data
import os
from dotenv import load_dotenv

def test_api_connection():
    # Carrega as variáveis de ambiente
    load_dotenv()
    
    # Obtém as credenciais
    api_url = os.getenv('API_URL')
    api_token = os.getenv('API_TOKEN')
    
    # Verifica se as credenciais foram carregadas
    assert api_url is not None, "API_URL não encontrada nas variáveis de ambiente"
    assert api_token is not None, "API_TOKEN não encontrada nas variáveis de ambiente"
    
    # Faz a requisição para a API
    data = fetch_data(api_url, api_token)
    
    # Verifica se a resposta não é None
    assert data is not None, "A API retornou None"
    
    # Verifica se a resposta é uma lista
    assert isinstance(data, list), "A resposta da API não é uma lista"
    
    # Se houver dados, verifica a estrutura
    if data:
        first_row = data[0]
        print("\nPrimeira linha de dados:")
        print(first_row)
        
        # Verifica se os campos necessários existem
        required_fields = ['atrasadas', 'nao_realizadas', 'pendentes', 'realizadas']
        for field in required_fields:
            assert field in first_row, f"Campo '{field}' não encontrado nos dados"
    
    print("\nTeste da API concluído com sucesso!")
    print(f"Total de registros encontrados: {len(data) if data else 0}") 