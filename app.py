import streamlit as st
import pandas as pd
import altair as alt

# Cargar datos
df = pd.read_csv("datos_limpios.csv")

st.set_page_config(page_title="Dashboard de Home Runs", layout="wide")
st.title("🏀 Dashboard de Jugadores de Béisbol")

# Filtro por equipo
equipos = df['team'].unique()
equipo_seleccionado = st.sidebar.multiselect("Selecciona equipo(s):", equipos, default=equipos)

# Filtrar datos
df_filtrado = df[df['team'].isin(equipo_seleccionado)]

# Mostrar tabla
st.subheader("Tabla de Jugadores")
st.dataframe(df_filtrado, use_container_width=True)

# Métricas principales
col1, col2, col3 = st.columns(3)
col1.metric("Total HR", int(df_filtrado['hr_total'].sum()))
col2.metric("HR Promedio por Jugador", round(df_filtrado['hr_total'].mean(), 1))
col3.metric("Promedio HR trot (s)", round(df_filtrado['avg_hr_trot'].mean(), 2))

# Gráfica de barras
st.subheader("Home Runs Totales por Jugador")
barras = alt.Chart(df_filtrado).mark_bar().encode(
    x=alt.X('player', sort='-y', title='Jugador'),
    y=alt.Y('hr_total', title='Total HR'),
    color='team'
).properties(width=800, height=400)

st.altair_chart(barras, use_container_width=True)

# Diagrama de dispersión
st.subheader("HR Totales vs HR Esperados")
dispersion = alt.Chart(df_filtrado).mark_circle(size=100).encode(
    x=alt.X('xhr', title='HR Esperados'),
    y=alt.Y('hr_total', title='HR Totales'),
    tooltip=['player', 'team', 'hr_total', 'xhr'],
    color='team'
).interactive().properties(width=800, height=400)

st.altair_chart(dispersion, use_container_width=True)

st.caption("Fuente: datos_limpios.csv")
