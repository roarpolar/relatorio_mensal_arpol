import streamlit as st
from PIL import Image
import os

def create_navbar():
    # Configuração do layout
    st.markdown("""
        <style>
        .navbar {
            width: 100%;
            padding: 0.8rem 1rem;
            margin: 0;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 9999;
            background-color: #0d47a1;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .navbar-content {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            max-width: 1200px;
            width: 100%;
            justify-content: center;
        }
        .logo-container {
            display: flex;
            align-items: center;
            margin-right: 1rem;
        }
        .logo-image {
            height: 50px;
            width: auto;
        }
        .company-name {
            color: white;
            font-size: 2rem;
            font-weight: bold;
            margin: 0;
            text-align: center;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    try:
        # Caminho da imagem
        image_path = "app_dash/assets/supervisores/Logo.png"
        
        if os.path.exists(image_path):
            # Container da navbar
            st.markdown('<div class="navbar">', unsafe_allow_html=True)
            
            # Container do conteúdo
            st.markdown('<div class="navbar-content">', unsafe_allow_html=True)
            
            # Logo
            st.markdown('<div class="logo-container">', unsafe_allow_html=True)
            st.image(image_path, 
                    width=50,
                    use_container_width=False)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Nome da empresa
            st.markdown('<h1 class="company-name">Arpol Quality Care</h1>', unsafe_allow_html=True)
            
            # Fechar os containers
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error(f"Arquivo não encontrado: {image_path}")
            
    except Exception as e:
        st.error(f"Erro ao carregar a navbar: {str(e)}") 