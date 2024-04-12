import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # lendo os dados

st.header(":sunglasses: Renan's First App Web :car:", divider='rainbow')

# criar uma caixa de seleção para gerar um histograma
build_hist = st.checkbox('Criar histograma')

if build_hist:  # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

# criar uma caixa de seleção para gerar um gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:  # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
