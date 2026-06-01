# almacenamiento.py
# Este módulo se encarga exclusivamente de la persistencia de datos en el disco.


def guardar_ranking_a_csv(conteo_datos, nombre_archivo="ranking_tecnologias.csv"):
    """Toma el conteo de Pandas, lo convierte a un archivo CSV

    para que pueda ser abierto en Excel.
    """
    # Usamos la función nativa que elegiste en el desafío
    conteo_datos.to_csv(nombre_archivo, header=["Cantidad"])