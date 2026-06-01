# Analizador de Mercado Tech — Paraguay

Herramienta para trackear y analizar tecnologías demandadas en ofertas de empleo tech para perfiles Junior y Trainee en Paraguay.

## ¿Qué hace?

Toma descripciones de puestos de trabajo, extrae las tecnologías mencionadas y genera métricas visuales sobre las más demandadas en el mercado local.

## Tecnologías

- Python 3.x
- Pandas
- Matplotlib
- Streamlit

## Estructura
├── datos.py          # Data cruda de ofertas
├── procesador.py     # Limpieza y análisis con Pandas
├── almacenamiento.py # Exportación a CSV
├── app.py            # Dashboard web (Streamlit)
└── main.py           # Menú interactivo por consola
## Cómo ejecutar

**Dashboard web:**
```bash
streamlit run app.py
```

**Consola:**
```bash
python main.py
```

## Instalación

```bash
pip install pandas matplotlib streamlit