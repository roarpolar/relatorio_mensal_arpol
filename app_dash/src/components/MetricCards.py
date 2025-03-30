import streamlit as st
from PIL import Image
import os

def create_metric_cards(atrasadas, nao_realizadas, pendentes, realizadas):
    """
    Cria os cards de métricas com os dados fornecidos.
    """
    # Estilo CSS para os cards
    st.markdown("""
        <style>
        .metric-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1.5rem;
            padding: 1rem;
            flex-wrap: nowrap;
            max-width: 1200px;
            margin: 0 auto;
            overflow-x: auto;
            width: 100%;
        }
        
        .metric-card {
            background-color: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
            min-width: 200px;
            max-width: 250px;
            flex: 0 1 auto;
            transition: transform 0.3s ease;
            margin: 0.5rem;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
        }
        
        .metric-value {
            font-size: 2.5em;
            font-weight: bold;
            margin: 0.5rem 0;
            color: #1f1f1f;
        }
        
        .metric-label {
            font-size: 1.1em;
            color: #666;
            margin: 0;
        }
        
        .metric-icon {
            font-size: 2em;
            margin-bottom: 0.5rem;
        }
        
        /* Cores específicas para cada tipo de métrica */
        .atrasadas { color: #dc3545; }
        .nao-realizadas { color: #ffc107; }
        .pendentes { color: #17a2b8; }
        .realizadas { color: #28a745; }
        
        /* Ajuste do container principal */
        .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            margin: 0 auto;
        }
        
        /* Ajuste do espaçamento entre os cards */
        .element-container {
            margin-bottom: 0;
            width: 100%;
        }

        /* Ajuste para garantir que os cards fiquem em uma linha */
        .stMarkdown {
            margin: 0;
            padding: 0;
            width: 100%;
        }

        /* Ajuste para centralizar o conteúdo */
        .stColumns {
            justify-content: center;
            width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    # Container para os cards
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)

    # Card de Atividades Atrasadas
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon atrasadas">⚠️</div>
            <div class="metric-value atrasadas">{atrasadas}</div>
            <div class="metric-label">Atividades Atrasadas</div>
        </div>
    """, unsafe_allow_html=True)

    # Card de Atividades Não Realizadas
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon nao-realizadas">❌</div>
            <div class="metric-value nao-realizadas">{nao_realizadas}</div>
            <div class="metric-label">Atividades Não Realizadas</div>
        </div>
    """, unsafe_allow_html=True)

    # Card de Atividades Pendentes
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon pendentes">⏳</div>
            <div class="metric-value pendentes">{pendentes}</div>
            <div class="metric-label">Atividades Pendentes</div>
        </div>
    """, unsafe_allow_html=True)

    # Card de Atividades Realizadas
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon realizadas">✅</div>
            <div class="metric-value realizadas">{realizadas}</div>
            <div class="metric-label">Atividades Realizadas</div>
        </div>
    """, unsafe_allow_html=True)

    # Fechar o container
    st.markdown('</div>', unsafe_allow_html=True)

def create_metric_card(supervisor):
    # Configuração do estilo do card
    st.markdown("""
        <style>
        .metric-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            margin: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            width: 100%;
            min-width: 300px;
        }
        .metric-card-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        .metric-card-title {
            font-size: 1.2rem;
            font-weight: bold;
            color: #333;
            margin: 0;
        }
        .metric-card-content {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        .metric-value {
            font-size: 1.5rem;
            font-weight: bold;
            color: #0d47a1;
        }
        .metric-label {
            color: #666;
            font-size: 0.9rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    try:
        # Caminho da imagem
        image_path = f"app_dash/assets/supervisores/{supervisor['name']}.png"
        
        if os.path.exists(image_path):
            # Container do card
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            
            # Cabeçalho do card
            st.markdown('<div class="metric-card-header">', unsafe_allow_html=True)
            
            # Foto do supervisor
            st.image(image_path, 
                    width=50,
                    use_container_width=False)
            
            # Nome do supervisor
            st.markdown(f'<h3 class="metric-card-title">{supervisor["name"]}</h3>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Conteúdo do card
            st.markdown('<div class="metric-card-content">', unsafe_allow_html=True)
            
            # Métricas
            st.markdown(f'<div class="metric-value">{supervisor["metrics"]["total"]}</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Total de Métricas</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error(f"Arquivo não encontrado: {image_path}")
            
    except Exception as e:
        st.error(f"Erro ao carregar o card: {str(e)}") 