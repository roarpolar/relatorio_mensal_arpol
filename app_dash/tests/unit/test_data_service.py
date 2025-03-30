import pytest
from datetime import datetime
from src.services.data_service import DataService

@pytest.fixture
def data_service():
    return DataService()

def test_fetch_data(data_service):
    # Teste com data atual
    date = datetime.now()
    result = data_service.fetch_data(date)
    assert result is not None

def test_get_metrics(data_service):
    # Teste com data atual
    date = datetime.now()
    metrics = data_service.get_metrics(date)
    assert isinstance(metrics, dict)
    assert all(key in metrics for key in ['atrasadas', 'nao_realizadas', 'pendentes', 'realizadas'])
    assert all(isinstance(value, int) for value in metrics.values()) 