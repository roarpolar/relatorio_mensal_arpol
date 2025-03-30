import streamlit as st
import os
from PIL import Image

def create_sidebar_buttons():
    # Estilo CSS para centralização
    st.markdown("""
        <style>
        .sidebar-title {
            text-align: center;
            margin-bottom: 20px;
        }
        .sidebar-image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }
        .stButton button {
            width: 100%;
            margin-bottom: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título centralizado
    st.markdown('<h1 class="sidebar-title">Supervisores</h1>', unsafe_allow_html=True)
    
    # Container para a imagem centralizada
    st.markdown('<div class="sidebar-image-container">', unsafe_allow_html=True)
    
    # Dicionário com os supervisores e suas fotos
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

    # Foto do supervisor selecionado
    if 'supervisor_photo' in st.session_state:
        try:
            photo_path = st.session_state['supervisor_photo']
            if os.path.exists(photo_path):
                # Abre e redimensiona a imagem
                image = Image.open(photo_path)
                # Calcula o novo tamanho mantendo a proporção
                max_width = 100  # Largura máxima em pixels
                ratio = max_width / image.width
                new_height = int(image.height * ratio)
                image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
                
                st.image(
                    image,
                    caption=st.session_state.get('selected_supervisor', ''),
                    use_container_width=True
                )
            else:
                st.error(f"Foto não encontrada para {st.session_state.get('selected_supervisor', '')}")
        except Exception as e:
            st.error(f"Erro ao carregar foto do supervisor: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Botões dos supervisores
    for name, photo in supervisors.items():
        if st.button(name, key=f"supervisor_{name}"):
            st.session_state['selected_supervisor'] = name
            st.session_state['supervisor_photo'] = photo
            st.rerun()

    return (
        st.session_state.get('selected_supervisor', 'Danielle'),
        st.session_state.get('supervisor_photo', 'app_dash/assets/supervisores/Danielle.png')
    ) 