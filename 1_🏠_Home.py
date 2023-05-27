# Libraries
import streamlit as st
import datetime
from datetime import datetime
import openpyxl

# bibliotecas necessarias
import pandas as pd
from PIL import Image
from streamlit_folium import folium_static


#======================================================================================================================
# Side Bar Streamlit
#======================================================================================================================
#image_path = '/Users/fabiomachida/Comunidade DS/repos/poupatempo/extrato_ponto/logo.png'
image = Image.open('logo.png')
st.sidebar.image(image, width=250)

st.sidebar.markdown('# Rh Data Science')

st.sidebar.markdown("""----""")

# Lê o arquivo de texto em um DataFrame
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo em texto", type=["txt"])

# Se o usuário fez upload de um arquivo
if uploaded_file is not None:
    # Lê o conteúdo do arquivo em um DataFrame do Pandas
    df = pd.read_csv(uploaded_file, delimiter='\t')
    # Exibe o DataFrame na tela
    #st.write(df)
    
st.title('Rh Data Science')

st.markdown(
    """ 
    Esse Dashboard foi construido para acompanhar a presença e ausencia dos Colaboradores.
    ### Como utilizar esse Rh Data?
    - **Importação dos dados:** 
        - Abra o App do relógio de ponto baixe e o arquivo no formato "txt".
        - Faça o "Upload" e analize os dados. 

    ### Ask for help
    - Consultar a Administração:
        - @LeonardoDelVechio
        - @IvoneSantos
    
""")

st.markdown("""----""") 
