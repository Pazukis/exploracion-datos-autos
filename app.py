import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de anuncios de venta de coches en EE. UU.")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Filtro por tipo de combustible

st.sidebar.header("Filtros")

fuel_types = car_data['fuel'].dropna().unique()
selected_fuels = st.sidebar.multiselect('Tipo de combustible:', fuel_types, default=fuel_types)

# Filtrar dataset
filtered_data = car_data[car_data['fuel'].isin(selected_fuels)]

st.subheader("Indicadores clave")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cantidad de vehículos", value=len(filtered_data))

with col2:
    avg_price = int(filtered_data['price'].mean())
    st.metric("Precio promedio", f"${avg_price:,}")

with col3:
    avg_odometer = int(filtered_data['odometer'].mean())
    st.metric("Odómetro promedio", f"{avg_odometer:,} millas")

# Casilla: mostrar histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma de odómetro para los coches seleccionados:')
    fig = px.histogram(filtered_data, x='odometer', color='fuel', barmode='overlay')
    st.plotly_chart(fig, use_container_width=True)

# Casilla: mostrar gráfico de dispersión
if st.checkbox('Mostrar dispersión entre odómetro y precio'):
    st.write('Gráfico de dispersión entre odómetro y precio:')
    fig = px.scatter(filtered_data, x='odometer', y='price', color='fuel')
    st.plotly_chart(fig, use_container_width=True)
    
# Casilla: mostrar boxplot (precio por tipo de combustible)
if st.checkbox('Mostrar boxplot de precios por tipo de combustible'):
    st.write("Comparación de precios según el tipo de combustible:")
    fig = px.box(
        filtered_data,
        x='fuel',
        y='price',
        color='fuel',
        points='all',  # para mostrar todos los puntos sobre la caja
        title='Distribución de precios por tipo de combustible'
    )
    st.plotly_chart(fig, use_container_width=True)