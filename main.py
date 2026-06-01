# main.py
# Director de orquesta con Menú Interactivo de Consola.

import matplotlib.pyplot as plt
import pandas as pd

# Importamos las herramientas de nuestros módulos locales
from almacenamiento import guardar_ranking_a_csv
from datos import lista_empleos
from procesador import obtener_ranking_tecnologias

# Cargamos los datos una sola vez al iniciar el programa
datos_crudos = lista_empleos
ranking = obtener_ranking_tecnologias(datos_crudos)

# ==========================================
# BUCLE PRINCIPAL DEL MENÚ (Opción A)
# ==========================================
while True:
    print("\n=============================================")
    print("   SISTEMA INTERACTIVO DE ANÁLISIS TECH 🇵🇾   ")
    print("=============================================")
    print("1. Ver la tabla completa de ofertas (Pandas DataFrame)")
    print("2. Ver el ranking numérico de tecnologías")
    print("3. Exportar resultados a archivo Excel (CSV)")
    print("4. Generar y visualizar reporte gráfico")
    print("5. Salir del programa")
    print("=============================================")

    # Le pedimos al usuario que ingrese su opción
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        print("\n[INFO] Cargando DataFrame original...")
        # Convertimos rápido a DataFrame solo para mostrar la tabla limpia
        df_completo = pd.DataFrame(datos_crudos)
        print(df_completo)

    elif opcion == "2":
        print("\n--- RANKING DE TECNOLOGÍAS MÁS DEMANDADAS ---")
        print(ranking)

    elif opcion == "3":
        print("\n[INFO] Exportando datos...")
        nombre_csv = "resultado_mercado.csv"
        guardar_ranking_a_csv(ranking, nombre_csv)
        print(f"[ÉXITO] Archivo '{nombre_csv}' generado en tu carpeta.")

    elif opcion == "4":
        print("\n[INFO] Generando gráfico de barras...")
        ranking.plot(
            kind="bar", color="lightgreen", edgecolor="black", figsize=(8, 5)
)
        plt.title("Tecnologías más demandadas (Modo Interactivo)")
        plt.xlabel("Tecnologías")
        plt.ylabel("Cantidad de Ofertas")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("ranking_interactivo.png")
        print("[ÉXITO] Gráfico guardado como 'ranking_interactivo.png'.")
        print("[INFO] Abriendo ventana del gráfico... (Cérrala para continuar)")
        plt.show()

    elif opcion == "5":
        print("\n¡Gracias por usar el sistema, Iván! Éxitos en tus estudios. ¡Chau!")
        break  # Rompe el bucle infinito y termina el programa de forma limpia

    else:
        print(
            "\n[ERROR] Opción no válida. Por favor, ingresá un número del 1 al 5."
        )