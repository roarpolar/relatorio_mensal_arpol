import streamlit as st
import os
import sys

# Adiciona o diretório atual ao PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Configura o diretório de assets
assets_dir = os.path.join(current_dir, 'assets')
if assets_dir not in sys.path:
    sys.path.append(assets_dir)

from src.components.Navbar import create_navbar
from src.components.Sidebar import create_sidebar
from src.components.MetricCards import create_metric_cards
from src.components.ButtonSiderbar import create_sidebar_buttons
from api.relatorio import fetch_data
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Arpol Quality Care - Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuração do CSS global
st.markdown("""
    <style>
    .main {
        padding-top: 4rem;
    }
    .stApp {
        padding-top: 4rem;
    }
    .stMarkdown {
        margin: 0;
        padding: 0;
    }
    .stColumns {
        justify-content: center;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Inicialização do estado da sessão
if 'selected_supervisor' not in st.session_state:
    st.session_state.selected_supervisor = "Danielle"

# Carregar dados da API
data = fetch_data()

# Criar Navbar
create_navbar()

# Layout principal
col1, col2 = st.columns([1, 4])

with col1:
    # Criar Sidebar
    selected_month = create_sidebar()
    # Criar botões dos supervisores na sidebar
    selected_supervisor = create_sidebar_buttons()

with col2:
    # Criar cards de métricas
    if data:
        # Criar 4 colunas para os cards
        metric_cols = st.columns(4)
        
        # Distribuir os cards nas colunas
        with metric_cols[0]:
            st.metric(
                label="Atividades Atrasadas",
                value=data.get('atrasadas', 0),
                delta=None
            )
        
        with metric_cols[1]:
            st.metric(
                label="Atividades Não Realizadas",
                value=data.get('nao_realizadas', 0),
                delta=None
            )
        
        with metric_cols[2]:
            st.metric(
                label="Atividades Pendentes",
                value=data.get('pendentes', 0),
                delta=None
            )
        
        with metric_cols[3]:
            st.metric(
                label="Atividades Realizadas",
                value=data.get('realizadas', 0),
                delta=None
            )
    else:
        st.error("Não foi possível carregar os dados da API") 