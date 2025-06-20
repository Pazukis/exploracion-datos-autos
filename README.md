# Análisis de anuncios de venta de coches en EE. UU.

Por Paz Emmanuel Balderas Cerezo.

Este repositorio contiene una aplicación web desarrollada con Streamlit como parte del Sprint 7 del bootcamp. La app permite analizar datos de vehículos en venta en EE. UU., explorando odómetro, precios y tipo de combustible de forma visual e interactiva.

El objetivo es construir una **aplicación web interactiva** que permita explorar datos sobre anuncios de vehículos en Estados Unidos utilizando `Streamlit`.

## Descripción de la aplicación
La aplicación permite a los usuarios:

- Filtrar los vehículos por tipo de combustible.
- Visualizar el odómetro de los vehículos mediante un **histograma**.
- Analizar la relación entre odómetro y precio mediante un **gráfico de dispersión**.
- Explorar la distribución del precio por tipo de combustible con un **gráfico de cajas (boxplot)**.
- Consultar **métricas clave** como el precio promedio, millaje promedio y cantidad de vehículos disponibles.

Todos los gráficos son interactivos y se actualizan dinámicamente en función de los filtros seleccionados.

## Tecnologías utilizadas
- `Python 3.11`
- `pandas`
- `plotly-express`
- `streamlit`

## Cómo ejecutar la app localmente
1. Clona este repositorio:
    git clone https://github.com/Pazukis/exploracion-datos-autos.git
2. Crea y activa un entorno virtual:
    conda create -n autos_env python=3.11
    conda activate autos_env
3. Instala las dependencias:
    pip install -r requirements.txt
4. Ejecuta la aplicación:
    streamlit run app.py

### Estructura del proyecto
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb