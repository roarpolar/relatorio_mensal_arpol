import streamlit as st
from datetime import datetime
import os
from PIL import Image
import requests
from io import BytesIO

def create_sidebar():
    st.sidebar.title("Filtros")
    
    # Seleção de mês
    current_month = datetime.now().month
    months = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    
    selected_month = st.sidebar.selectbox(
        "Selecione o Mês",
        options=list(months.keys()),
        format_func=lambda x: months[x],
        index=current_month - 1
    )
    
    return selected_month

# Alternativa usando URLs de placeholder
