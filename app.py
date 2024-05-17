import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title('Análisis de Anuncios de Venta de Coches - Jorge Carrillo')

# Leer el archivo CSV del conjunto de datos en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar una pequeña muestra del DataFrame para confirmar la carga de datos
st.write("Muestra del conjunto de datos:", car_data.head())

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir histograma')

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

# Encabezado para las visualizaciones
st.header('Visualizaciones')

# Construir el histograma si la casilla de verificación está seleccionada
if build_histogram:
    st.subheader('Histograma del Kilometraje de los Coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Construir el gráfico de dispersión si la casilla de verificación está seleccionada
if build_scatter:
    st.subheader('Gráfico de Dispersión de Precio vs. Kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price", color="condition", title="Gráfico de dispersión de precio vs. kilometraje")
    st.plotly_chart(fig, use_container_width=True)
