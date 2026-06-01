# procesador.py
# Este módulo contiene la lógica de negocio para procesar datos usando Pandas.

import pandas as pd


def obtener_ranking_tecnologias(lista_datos):
    """Recibe una lista de diccionarios, la procesa con Pandas

    y devuelve el conteo de tecnologías ordenadas.
    """
    # Convertimos la lista recibida en un DataFrame
    df = pd.DataFrame(lista_datos)

    # Aplicamos la lógica de Pandas para romper las listas y contar
    df_explotado = df["tecnologias"].explode()
    conteo_tech = df_explotado.value_counts()

    return conteo_tech