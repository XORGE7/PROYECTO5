import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title('Análisis de Anuncios de Venta de Coches - Jorge Carrillo')

# Leer el archivo CSV del conjunto de datos en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Manejo de datos faltantes: eliminar filas con datos faltantes en las columnas clave
car_data = car_data.dropna(subset=['model_year', 'condition', 'fuel', 'price'])

# Mostrar una pequeña muestra del DataFrame para confirmar la carga de datos
st.write("Muestra del conjunto de datos:", car_data.head(30))

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir histograma')

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

# Casilla de verificación para construir un gráfico de barras del precio promedio
build_bar = st.checkbox('Construir gráfico de barras del precio promedio')

# Casilla de verificación para construir un histograma de kilometraje por modelo
build_kilometraje_hist = st.checkbox('Construir histograma de kilometraje por modelo')

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

# Construir el gráfico de barras del precio promedio si la casilla de verificación está seleccionada
if build_bar:
    st.subheader('Gráfico de Barras del Precio Promedio por Año, Condición y Tipo de Combustible')
    # Preparar los datos: agrupar por año del modelo, condición y tipo de combustible, y calcular el precio promedio
    price_avg = car_data.groupby(['model_year', 'condition', 'fuel'])['price'].mean().reset_index()
    price_avg.columns = ['model_year', 'condition', 'fuel', 'average_price']
    # Crear el gráfico de barras usando los datos preparados
    fig = px.bar(
        price_avg,
        x='model_year',
        y='average_price',
        color='condition',
        barmode='group',
        facet_col='fuel',
        title="Precio promedio por año del modelo, condición y tipo de combustible",
        labels={'model_year': 'Año del Modelo', 'average_price': 'Precio Promedio', 'condition': 'Condición', 'fuel': 'Tipo de Combustible'}
    )
    # Mejorar el diseño del gráfico
    fig.update_layout(
        xaxis_title="Año del Modelo",
        yaxis_title="Precio Promedio",
        legend_title="Condición",
        title={
            'text': "Precio promedio por año del modelo, condición y tipo de combustible",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="RebeccaPurple"
        )
    )
    st.plotly_chart(fig, use_container_width=True)

# Construir el histograma de kilometraje por modelo si la casilla de verificación está seleccionada
if build_kilometraje_hist:
    st.subheader('Histograma del Kilometraje por Modelo de Coche')
    fig = px.histogram(
        car_data,
        x='model',
        y='odometer',
        title='Kilometraje por Modelo de Coche',
        labels={
            'model': 'Modelo de Coche',
            'odometer': 'Kilometraje'
        }
    )
    # Mejorar el diseño del gráfico
    fig.update_layout(
        xaxis_title='Modelo de Coche',
        yaxis_title='Kilometraje',
        title={
            'text': "Kilometraje por Modelo de Coche",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="RebeccaPurple"
        )
    )
    st.plotly_chart(fig, use_container_width=True)
