import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV del conjunto de datos en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir histograma')

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

# Construir el histograma si la casilla de verificación está seleccionada
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Construir el gráfico de dispersión si la casilla de verificación está seleccionada
if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price", color="condition", title="Gráfico de dispersión de precio vs. kilometraje")
    st.plotly_chart(fig, use_container_width=True)