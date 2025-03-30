import requests
from functools import lru_cache
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from ..config.settings import settings

class DataService:
    def __init__(self):
        self.api_url = settings.API_URL
        self.api_token = settings.API_TOKEN
        self.headers = {'Authorization': f'Bearer {self.api_token}'}
    
    @lru_cache(maxsize=128)
    def fetch_data(self, date: datetime) -> Optional[Dict[str, Any]]:
        """
        Busca dados da API com cache
        """
        try:
            response = requests.get(
                self.api_url,
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados: {str(e)}")
            return None
    
    def get_metrics(self, date: datetime) -> Dict[str, int]:
        """
        Processa os dados e retorna as métricas
        """
        data = self.fetch_data(date)
        if not data:
            return {
                'atrasadas': 0,
                'nao_realizadas': 0,
                'pendentes': 0,
                'realizadas': 0
            }
        
        # Aqui você deve implementar a lógica de processamento dos dados
        # Este é apenas um exemplo
        return {
            'atrasadas': data.get('atrasadas', 0),
            'nao_realizadas': data.get('nao_realizadas', 0),
            'pendentes': data.get('pendentes', 0),
            'realizadas': data.get('realizadas', 0)
        } 