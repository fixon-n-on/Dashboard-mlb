import streamlit as st
import pandas as pd
import altair as alt

# Título del dashboard
st.title("Dashboard de Jonrones por Jugador")

# Cargar los datos (forzamos la codificación para evitar errores)
try:
    df = pd.read_csv("datos_limpio.csv", encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv("datos_limpio.csv", encoding="latin1")

# Mostrar los primeros registros
st.subheader("Vista previa de los datos")
st.dataframe(df)

# Filtro por equipo
equipos = df["team"].unique()
equipo_seleccionado = st.selectbox("Selecciona un equipo", equipos)

# Filtrar el DataFrame por el equipo seleccionado
df_filtrado = df[df["team"] == equipo_seleccionado]

# Gráfico: HR Totales por Jugador
st.subheader(f"HR Totales del equipo {equipo_seleccionado}")
grafico = alt.Chart(df_filtrado).mark_bar().encode(
    x=alt.X("player", sort="-y"),
    y="hr_total",
    tooltip=["player", "hr_total"]
).properties(width=600, height=400)

st.altair_chart(grafico)

# Mostrar métricas por jugador
st.subheader("Estadísticas individuales")
jugador = st.selectbox("Selecciona un jugador", df_filtrado["player"])
jugador_data = df_filtrado[df_filtrado["player"] == jugador].iloc[0]

st.metric("Avg HR Trot", jugador_data["avg_hr_trot"])
st.metric("Doubters", jugador_data["doubters"])
st.metric("No Doubters", jugador_data["no_doubters"])
st.metric("HR Total", jugador_data["hr_total"])
st.metric("xHR", jugador_data["xhr"])
