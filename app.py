import streamlit as st
import pandas as pd

# Lendo os dados de um arquivo CSV


@st.cache
def load_data():
    data = pd.read_csv('vehicles_us.csv')
    return data


data = load_data()

st.title('Análise de Veículos')

# Filtro de seleção múltipla para a marca do veículo
marcas = st.multiselect('Escolha a(s) marca(s)', options=data['manufacturer'].unique(
), default=data['manufacturer'].unique())

# Filtro de intervalo para o ano do veículo
ano_min, ano_max = st.slider('Escolha o intervalo de anos', int(data['year'].min(
)), int(data['year'].max()), (int(data['year'].min()), int(data['year'].max())))

# Filtro de faixa de preço
preco_min, preco_max = st.slider('Escolha o intervalo de preços', int(data['price'].min(
)), int(data['price'].max()), (int(data['price'].min()), int(data['price'].max())))

# Aplicando os filtros aos dados
data_filtrada = data[
    (data['manufacturer'].isin(marcas)) &
    (data['year'] >= ano_min) & (data['year'] <= ano_max) &
    (data['price'] >= preco_min) & (data['price'] <= preco_max)
]

st.write(f'Dados Filtrados ({data_filtrada.shape[0]} linhas)')
st.dataframe(data_filtrada)

# Exibindo um gráfico de dispersão dos dados filtrados
st.write('Gráfico de dispersão do odômetro vs. preço')
st.plotly_chart(px.scatter(data_filtrada, x='odometer', y='price'))
