# app.py
# Interfaz Web Interactiva (Dashboard) usando Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Reutilizamos la arquitectura modular que ya construiste
from datos import lista_empleos
from procesador import obtener_ranking_tecnologias

# Configuración de la página web
st.set_page_config(page_title="Tech Market Analizer PY", page_icon="📊", layout="wide")

# Título principal en la web
st.title("📊 Análisis de Mercado Tech en Paraguay")
st.markdown("### Reporte interactivo para perfiles Junior y Trainee")

# Cargamos los datos compartidos
datos_crudos = lista_empleos
ranking = obtener_ranking_tecnologias(datos_crudos)
df_completo = pd.DataFrame(datos_crudos)

# ==========================================
# BARRA LATERAL (Filtros Interactivos)
# ==========================================
st.sidebar.header("Filtros y Acciones")
st.sidebar.markdown("Interactúa con el sistema en tiempo real.")

# Botón para descargar el CSV directo desde la web (Persistencia)
csv_data = ranking.to_csv(header=["Cantidad"]).encode('utf-8')
st.sidebar.download_button(
    label="📥 Descargar Reporte en Excel (CSV)",
    data=csv_data,
    file_name="reporte_mercado_py.csv",
    mime="text/csv",
)

# ==========================================
# CUERPO PRINCIPAL (Dashboard)
# ==========================================
# Creamos dos columnas visuales en la página web
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Ofertas de Empleo Detectadas")
    st.write("Datos estructurados cargados desde el backend:")
    # Muestra la tabla de Pandas como una tabla web interactiva donde se puede ordenar
    st.dataframe(df_completo, use_container_width=True)

with col2:
    st.subheader("📈 Ranking de Demandas")
    
    # Renderizamos el gráfico de Matplotlib directo en la página web
    fig, ax = plt.subplots(figsize=(6, 4))
    ranking.plot(kind="bar", color="lightgreen", edgecolor="black", ax=ax)
    plt.title("Tecnologías más solicitadas")
    plt.xlabel("Tecnologías")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # El truco mágico de Streamlit para mostrar gráficos
    st.pyplot(fig)

# Un mensaje final amigable
st.info("💡 Desarrollado de forma modular en Python utilizando Pandas, Matplotlib y Streamlit.")