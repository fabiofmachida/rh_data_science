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
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo em texto", type=["txt"], disabled=True)

# Se o usuário fez upload de um arquivo
if uploaded_file is not None:
    # Lê o conteúdo do arquivo em um DataFrame do Pandas
    df = pd.read_csv(uploaded_file, delimiter='\t')
    # Exibe o DataFrame na tela
    #st.write(df)
    
st.title('Licença Maternidade')

st.markdown("""----""")   

@st.cache_resource
def get_lista():
    # Crie uma lista vazia para armazenar os itens
    lista = []
    return lista

# Obtenha a lista do cache ou gere uma nova lista
lista = get_lista()

# Adicione um campo de entrada de texto e um botão "Adicionar" para adicionar itens à lista
item = st.text_input("Digite um item para adicionar à lista:")
if st.button("Adicionar"):
    if item:
        lista.append(item)
        st.write("Item adicionado à lista.")


# Adicione um campo de entrada de texto e um botão "Remover" para remover itens da lista
remover = st.text_input("Digite um item para remover da lista:")
if st.button("Remover"):
    if remover in lista:
        lista.remove(remover)
        st.write("Item removido da lista.")

# Salve a lista no cache
st.cache()
get_lista()

data = pd.DataFrame(lista)
data = data.rename(columns={0: 'COLABORADORAS'})

# Exiba a lista atualizada
st.markdown('## Colaboradoras em Licença Maternidade')
st.write(data)
