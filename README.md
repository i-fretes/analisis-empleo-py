 # Análisis de Empleos Tech en Paraguay 🇵🇾

## 🎯 Objetivo del Proyecto
Este proyecto nace de una problemática real: los desarrolladores Junior/Trainee muchas veces no saben qué tecnologías priorizar para insertarse en el mercado laboral local. 

El objetivo es procesar y analizar ofertas de empleo tecnológico en Paraguay para identificar de forma basada en datos cuáles son las herramientas más demandadas, las modalidades de trabajo predominantes (Remoto/Híbrido/Presencial) y presentar los resultados de forma visual.

---

## 🛠️ Tecnologías Utilizadas
* **Python** (Lógica de estructuración de datos y normalización de texto)
* **Pandas** (Manipulación avanzada de datos, limpieza y análisis estadístico)
* **Matplotlib** (Generación de reportes visuales y gráficos de barras)

---

## 📈 Resultados del Análisis Inicial (Piloto)

A partir de un set de datos de prueba basado en ofertas del mercado local, se procesaron las descripciones de los puestos (normalizando el texto a minúsculas para evitar duplicados por tipeo) y se extrajeron las siguientes conclusiones:

### 1. Top Tecnologías Demandadas
Según el conteo automatizado, **Python** y **SQL** lideran el requerimiento de los reclutadores para perfiles Backend y de Datos, seguidos por librerías de análisis como **Pandas**.

### 2. Visualización de Datos
El script genera automáticamente un reporte gráfico que se guarda localmente como `ranking_tecnologias.png`:

![Ranking de Tecnologías](ranking_tecnologias.png)

---

## 🚀 Cómo Ejecutar el Proyecto

1. Clonar el repositorio.
2. Instalar las dependencias necesarias ejecutando en la terminal:
   ```bash
   pip install pandas matplotlib
