import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo os dados de um arquivo CSV
@st.cache
def load_data():
    data = pd.read_csv('vehicles_us.csv')
    return data

data = load_data()

st.header(":sunglasses: Renan's First App Web :car:", divider='rainbow')

st.title('Análise de Veículos')

# Filtro de seleção múltipla para a marca do veículo
modelos = st.multiselect('Escolha o(s) modelos(s)', options=data['model'].unique(), default=data['model'].unique())

# Filtro de intervalo para o ano do veículo
ano_min, ano_max = st.slider('Escolha o intervalo de anos', int(data['model_year'].min()), int(data['model_year'].max()), (int(data['model_year'].min()), int(data['model_year'].max())))

# Filtro de faixa de preço
preco_min, preco_max = st.slider('Escolha o intervalo de preços', int(data['price'].min()), int(data['price'].max()), (int(data['price'].min()), int(data['price'].max())))

# Aplicando os filtros aos dados
data_filtrada = data[
    (data['model'].isin(modelos)) &
    (data['model_year'] >= ano_min) & (data['model_year'] <= ano_max) &
    (data['price'] >= preco_min) & (data['price'] <= preco_max)
]

st.write(f'Dados Filtrados ({data_filtrada.shape[0]} linhas)')
st.dataframe(data_filtrada)

# Exibindo um gráfico de dispersão dos dados filtrados
st.write('Gráfico de dispersão do odômetro vs. preço')
st.plotly_chart(px.scatter(data_filtrada, x='odometer', y='price'))


# criar uma caixa de seleção para gerar um histograma
build_hist = st.checkbox('Criar histograma')

if build_hist:  # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig_hist = px.histogram(data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)
    
    
    # criar uma caixa de seleção para gerar um gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:  # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig_scatter = px.scatter(data, x="odometer", y="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)