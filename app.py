#importamos librerias necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

#Importamos el DataFrame de vehiculos en USA
cars_df = pd.read_csv("vehicles_us.csv")

#Desarrollamos la aplicacion de streamlit
st.header('Vehiculos en U.S.A.')

histogram_button = st.button('Construir Histograma')
if histogram_button:
    #mostramos un mensaje
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')
    
    #Creamos el histograma
    fig = px.histogram(cars_df,x='odometer')

    #mostramos el grafico de plotly express
    st.plotly_chart(fig, use_container_width=True)
    
scatter_button = st.button('Construir Diagrama Dispersion')
if scatter_button:
    st.write('Diagrama de dispersion para Analizar la relacion de los Autos de USA y su precio')
    
    fig2 = px.scatter(cars_df,x='odometer',y='price')
    
    st.plotly_chart(fig2, use_container_width=True)