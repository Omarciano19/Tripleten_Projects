'''Modulo de la aplicación web del analisis estadistico simple
 de multiples anuncions de coches, muestreo y graficación.'''
import plotly.express as px
import pandas as pd
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header('Despliegue web de un análisis estadístico simple de anuncios de coches.')

num_samples = st.slider('Selecciona el número de muestras', 5, 200)

show_df = st.button('Mostrar muestra del DataFrame')

hist_check = st.checkbox('Construir histograma')  # crear un botón

disp_check = st.checkbox(
    'Construir grafico de dispersión')  # crear un checkbox

boxplot_check = st.checkbox(
    'Construir grafico de caja de precios')  # crear un checkbox

color_check = st.checkbox(
    'Averigua que colores son mas raros con este grafico de barras.')  # crear un checkbox

if show_df:
    st.write('Una muestra aleatoria de nuestro dataframe es:')
    car_sample = car_data.sample(num_samples)
    # Aplicar estilos al dataframe
    car_data_styled = car_sample.style.set_properties(**{'background-color': 'black',
                                                         'color': 'lawngreen',
                                                         'border-color': 'white'})
    st.write(car_data_styled)


if hist_check:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if disp_check:  # al verificar la checkbox
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersión comparando precios y año del modelo.')

    # crear un histograma
    fig2 = px.scatter(car_data, y="price", x="model_year")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)


if boxplot_check:  # al verificar la checkbox
    # escribir un mensaje
    st.write(
        'Creación de un grafico de caja para los precios de venta de coches')

    # crear un histograma
    fig = px.box(car_data, x="type", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if color_check:  # al verificar la checkbox
    # escribir un mensaje
    st.write('Creación de un histograma de los colores de autos:')

    # crear un histograma
    fig = px.histogram(car_data, x="paint_color")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
