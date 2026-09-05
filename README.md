# Portafolio de productos digitales — Gabriela Durán Vidal

<p align="center">
  <img src="https://avatars.githubusercontent.com/u/291106565?v=4" width="150" alt="Avatar de Gabriela Durán Vidal" />
</p>

## Sobre mí

Soy **Gabriela Durán Vidal**, psicóloga organizacional y clínica, con experiencia en gestión de personas y actualmente fortaleciendo mi perfil en **análisis de datos, People Analytics e inteligencia artificial aplicada a RR.HH.** Me interesa desarrollar soluciones tecnológicas que conviertan datos en evidencia útil para la toma de decisiones, manteniendo el criterio humano y la ética profesional en el centro.

### Enlaces profesionales

- [LinkedIn](https://cl.linkedin.com/in/gabrieladuranvidal)
- [GitHub](https://github.com/gabrieladuranv-collab)
- [Sitio profesional](https://gabrieladuran.cl)
- Correo: [gabriela.duranv@gmail.com](mailto:gabriela.duranv@gmail.com)

## Objetivo del repositorio

Este repositorio reúne trabajos desarrollados durante mi formación en análisis de datos e inteligencia artificial y funciona como **portafolio digital**. La estructura prioriza claridad, trazabilidad, reproducibilidad y navegación simple para que una persona evaluadora pueda identificar rápidamente el problema abordado, las herramientas utilizadas, el código y los resultados de cada trabajo.

## Proyectos incluidos

| Proyecto | Área | Herramientas | Estado |
|---|---|---|---|
| [Inferencia estadística](projects/inferencia-estadistica/) | Estadística aplicada | Python, NumPy, pandas, SciPy, Matplotlib | Validado localmente |
| [Aprendizaje no supervisado](projects/aprendizaje-no-supervisado/) | Machine Learning | scikit-learn, K-means, Silhouette, PCA | Validado localmente |
| [Perceptrón de mantenimiento](projects/perceptron-mantenimiento/) | Redes neuronales | Python, NumPy | Validado localmente |
| [Clasificador de sentimiento](projects/clasificador-sentimiento/) | Deep Learning / NLP | TensorFlow/Keras, scikit-learn, pandas | Requiere dataset externo del desafío |

## Evidencias destacadas

### Inferencia estadística

El trabajo simula 200 estudiantes, explora y trata valores nulos, analiza la distribución del puntaje de satisfacción, calcula un intervalo de confianza del 95% y realiza una prueba t de una muestra. El script genera automáticamente su histograma de resultados al ejecutarse.

### Aprendizaje no supervisado

El trabajo utiliza preprocesamiento, K-means y **Silhouette Score** para elegir el número de clusters, y luego aplica **PCA** para visualizar la segmentación en dos dimensiones. El script genera la visualización de clusters como archivo PNG.

## Buenas prácticas aplicadas

- Estructura de carpetas por proyecto.
- Nombres de archivos descriptivos y consistentes.
- README general y documentación específica por trabajo.
- Dependencias declaradas en `requirements.txt`.
- `.gitignore` para archivos locales, temporales y secretos.
- Semillas aleatorias en los ejercicios que requieren reproducibilidad.
- Separación entre código fuente, resultados y documentación.
- No se incluyen archivos de apoyo docente como si fueran trabajos propios.
- Se documentan explícitamente dependencias o datasets no entregados.

## Características y razones para usar GitHub

GitHub permite mantener **control de versiones**, conservar el historial de cambios, compartir un enlace único con evaluadores y reclutadores, organizar múltiples trabajos dentro de un mismo repositorio y publicar una versión navegable del portafolio mediante **GitHub Pages**. Estas características lo convierten en una opción adecuada para un portafolio técnico y profesional.

## Cómo ejecutar los proyectos

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
pip install -r requirements.txt
```

Después, entra a la carpeta del proyecto y ejecuta su archivo `.py`. Cada proyecto incluye instrucciones específicas.

## Documentación de la entrega

- [Planificación, criterios y mejoras aplicadas](docs/planificacion-portafolio.md)
- [Checklist de cumplimiento de rúbrica](docs/checklist-rubrica.md)
- [Versión web del portafolio](index.html)

---

**Autora:** Gabriela Durán Vidal  
**Formación:** Desafío Latam  
**Actualización:** septiembre de 2026
