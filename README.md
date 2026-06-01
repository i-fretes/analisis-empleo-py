# 📊 Analizador de Mercado Tech - Paraguay (`Junior/Trainee`)

¡Bienvenido! Este es un proyecto de grado profesional diseñado para trackear, limpiar y analizar las ofertas de empleo tecnológico en el mercado paraguayo, enfocado específicamente en los requerimientos para perfiles **Junior** y **Trainee**. 

El sistema transforma descripciones de puestos de trabajo desestructuradas en métricas visuales limpias, implementando una arquitectura desacoplada y un pipeline de datos interactivo.

---

## 🚀 Características Principales (Factor "Wow")
* **Arquitectura Modular:** Separación estricta de responsabilidades (Clean Architecture).
* **Análisis Vectorizado:** Procesamiento eficiente de tecnologías usando **Pandas** (`.explode()`, `.value_counts()`).
* **Robustez Empresarial (Error Handling):** Control de excepciones activo (`try-except`) contra bloqueos de archivos del Sistema Operativo (`PermissionError`).
* **Dual-Interface:** Selector de ejecución mediante **Menú Interactivo de Consola** o un **Dashboard Web Interactivo** moderno con **Streamlit**.
* **Persistencia Local:** Exportación automatizada de reportes tabulados directamente a formatos compatibles con Excel (`.csv`).

---

## 📁 Arquitectura y Estructura del Sistema

El software se diseñó bajo el principio de **Responsabilidad Única**, dividiendo el flujo en módulos independientes:

* 🗄️ **`datos.py` (Capa de Datos):** Gestiona la consistencia de la data cruda estructurada en diccionarios nativos.
* ⚙️ **`procesador.py` (Lógica de Negocio):** Realiza la limpieza, normalización de texto (*Case Normalization*) y transformaciones analíticas con Pandas.
* 💾 **`almacenamiento.py` (Capa de Persistencia):** Maneja la escritura en disco y funciona como escudo contra fallos de entorno si el usuario tiene los archivos abiertos.
* 🌐 **`app.py` (Frontend / Presentación Web):** Levanta un servidor gráfico interactivo con filtros, tablas dinámicas y descargas nativas usando Streamlit.
* 🚀 **`main.py` (Orquestador de Consola):** Mantiene un bucle infinito controlado (`while True`) para ejecutar el sistema directamente desde la terminal.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.x** (Lenguaje Core)
* **Pandas** (Data Manipulation & Analytics)
* **Matplotlib