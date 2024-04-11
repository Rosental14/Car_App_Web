import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # lendo os dados

st.header('My First App Web', divider='rainbow')

# criar um botão para gerar um histograma
hist_button = st.button('Criar histograma')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

# criar um botão para gerar um gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
