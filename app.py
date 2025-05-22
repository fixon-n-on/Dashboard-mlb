import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("datos_limpio.csv", encoding="latin1")

# Título
st.title("Dashboard de Jonrones por Jugador")

# Mostrar el dataframe
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(df)

# Seleccionar jugador
jugador = st.selectbox("Selecciona un jugador", df["player"].unique())
df_jugador = df[df["player"] == jugador]

# Gráficas
st.subheader(f"Estadísticas de {jugador}")

st.metric("Total de HR", int(df_jugador["hr_total"].values[0]))
st.metric("Doubters", int(df_jugador["doubters"].values[0]))
st.metric("No Doubters", int(df_jugador["no_doubters"].values[0]))

fig = px.bar(
    df_jugador.melt(id_vars=["player"], value_vars=["avg_hr_trot", "xhr"]),
    x="variable", y="value", color="variable",
    labels={"value": "Valor", "variable": "Métrica"}
)
st.plotly_chart(fig)
