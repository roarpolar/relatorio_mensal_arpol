import streamlit as st
import os
from PIL import Image

def create_sidebar_buttons():
    """
    Cria os botões dos supervisores na sidebar e gerencia a exibição da foto do supervisor selecionado.
    """
    # Estilo CSS para os botões na sidebar
    st.markdown("""
        <style>
        /* Estilo para o container da sidebar */
        .css-1d391kg {
            padding-top: 2rem;
        }
        
        /* Estilo para o título da seção */
        .supervisor-title {
            text-align: center;
            color: #1f1f1f;
            font-size: 1.5em;
            font-weight: 600;
            margin-bottom: 1.5em;
            padding-top: 1em;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 0.5em;
        }
        
        /* Estilo para o container da foto */
        .supervisor-photo {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 1.5em 0;
            padding: 0.5em;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Container para os botões */
        .button-container {
            display: flex;
            flex-direction: column;
            gap: 0.5em;
            padding: 0.5em;
            width: 100%;
            max-width: 250px;
            margin: 0 auto;
        }
        
        /* Estilo para os botões */
        .stButton button {
            width: 100%;
            min-height: 45px;
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            padding: 0.8em 1em;
            border-radius: 8px;
            text-align: center;
            transition: all 0.3s ease;
            font-weight: 500;
            color: #1f1f1f;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.95em;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            margin: 0;
            line-height: 1.2;
            min-width: 200px;
        }
        
        /* Hover effect para os botões */
        .stButton button:hover {
            background-color: #f8f9fa;
            border-color: #d0d0d0;
            transform: translateY(-1px);
            box-shadow: 0 2px 5px rgba(0,0,0,0.15);
        }
        
        /* Estilo para o botão selecionado */
        .stButton button[kind="secondary"] {
            background-color: #e6f3ff;
            border-color: #2196f3;
            color: #1976d2;
        }
        
        /* Ajuste do espaçamento entre os botões */
        .stButton {
            margin: 0;
            padding: 0;
            width: 100%;
            display: flex;
            justify-content: center;
        }
        
        /* Estilo para a legenda da foto */
        .stImage caption {
            text-align: center;
            font-weight: 500;
            color: #1f1f1f;
            margin-top: 0.5em;
        }

        /* Ajuste do container da sidebar */
        .css-1d391kg {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título da seção
    st.sidebar.markdown('<p class="supervisor-title">Supervisores</p>', unsafe_allow_html=True)

    # Lista de supervisores
    supervisors = {
        'Danielle': 'app_dash/assets/supervisores/Danielle.png',
        'Joel': 'app_dash/assets/supervisores/Joel.png',
        'Lucas': 'app_dash/assets/supervisores/Lucas.png',
        'Marcelo': 'app_dash/assets/supervisores/Marcelo.png',
        'Renato': 'app_dash/assets/supervisores/Renato.png',
        'Robson': 'app_dash/assets/supervisores/Robson.png',
        'Thiago': 'app_dash/assets/supervisores/Thiago.png',
        'Wanderson': 'app_dash/assets/supervisores/Wanderson.png',
        'Mário': 'app_dash/assets/supervisores/Mario.png',
        'Rafael': 'app_dash/assets/supervisores/Rafael.png',
        'Everton': 'app_dash/assets/supervisores/Everton.png'
    }

    # Container para a foto do supervisor
    photo_container = st.sidebar.container()

    # Exibir foto do supervisor atual
    if 'selected_supervisor' in st.session_state:
        current_supervisor = st.session_state.selected_supervisor
        photo_path = supervisors.get(current_supervisor)
        
        if photo_path and os.path.exists(photo_path):
            try:
                # Carregar e redimensionar a foto
                image = Image.open(photo_path)
                # Calcular dimensões mantendo proporção
                max_width = 180
                ratio = max_width / image.size[0]
                new_size = (max_width, int(image.size[1] * ratio))
                image = image.resize(new_size, Image.Resampling.LANCZOS)
                
                # Exibir a foto
                with photo_container:
                    st.markdown('<div class="supervisor-photo">', unsafe_allow_html=True)
                    st.image(image, caption=current_supervisor, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.sidebar.error(f"Erro ao carregar a foto: {str(e)}")

    # Container para os botões
    st.sidebar.markdown('<div class="button-container">', unsafe_allow_html=True)

    # Criar botões para cada supervisor
    for name in supervisors.keys():
        button_type = "secondary" if name == st.session_state.get('selected_supervisor', 'Danielle') else "primary"
        if st.sidebar.button(
            name,
            key=f"btn_{name}",
            help=f"Visualizar dados de {name}",
            type=button_type
        ):
            st.session_state.selected_supervisor = name
            st.rerun()

    st.sidebar.markdown('</div>', unsafe_allow_html=True)

    return st.session_state.get('selected_supervisor', 'Danielle')
