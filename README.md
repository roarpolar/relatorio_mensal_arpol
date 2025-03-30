# Dashboard Arpol Quality Care

Este é um dashboard desenvolvido com Streamlit para visualização de dados de preventivas da Arpol Quality Care.

## Estrutura do Projeto

```
├── README.md
├── app_dash
│   ├── __init__.py
│   ├── api
│   │   └── relatorios.py
│   ├── assets
│   │   ├── logo.png
│   │   └── supervisors/
│   └── src
│       ├── Components
│       │   ├── Navbar.py
│       │   ├── Sidebar.py
│       │   ├── MetricCards.py
│       │   └── SupervisorButtons.py
│       └── Styles
│           └── main.css
├── docs
├── poetry.lock
├── pyproject.toml
└── tests
```

## Requisitos

- Python 3.8+
- Poetry para gerenciamento de dependências
- Arquivo .env com as seguintes variáveis:
  - API_URL
  - API_TOKEN

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Instale as dependências usando Poetry:
```bash
poetry install
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

## Executando o Projeto

1. Ative o ambiente virtual:
```bash
poetry shell
```

2. Execute o dashboard:
```bash
streamlit run app_dash/main.py
```

## Funcionalidades

- Visualização de dados de preventivas por supervisor
- Seleção de mês para análise
- Métricas em tempo real:
  - Preventivas Atrasadas
  - Preventivas Não Realizadas
  - Preventivas Pendentes
  - Preventivas Realizadas
- Interface responsiva e moderna
- Integração com API de dados

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença [NOME_DA_LICENÇA].

