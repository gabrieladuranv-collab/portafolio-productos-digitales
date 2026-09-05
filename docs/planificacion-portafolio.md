# Planificación del portafolio digital

## 1. Propósito

Construir un repositorio profesional que concentre trabajos realizados durante la formación y permita a docentes, empresas o reclutadores revisar rápidamente evidencia de habilidades técnicas, capacidad de análisis y documentación.

## 2. Público objetivo

- Docente evaluador/a del desafío.
- Reclutadores/as y equipos TI o de datos.
- Personas interesadas en proyectos de People Analytics, analítica e inteligencia artificial aplicada.

## 3. Características definidas para el repositorio

1. **Accesibilidad:** navegación directa desde un README principal.
2. **Orden:** una carpeta por proyecto, evitando archivos dispersos.
3. **Trazabilidad:** documentación del objetivo, metodología y resultados.
4. **Reproducibilidad:** dependencias declaradas y uso de semillas cuando corresponde.
5. **Legibilidad:** nombres de archivos claros, comentarios en el código y secciones coherentes.
6. **Seguridad básica:** `.gitignore` para evitar publicar secretos, entornos virtuales o archivos temporales.
7. **Portabilidad:** instrucciones de instalación y ejecución con Python.
8. **Presentación profesional:** portada web estática preparada para GitHub Pages.

## 4. Razones para elegir GitHub

- Es un estándar ampliamente utilizado en desarrollo de software y análisis de datos.
- Permite compartir el trabajo mediante un enlace único.
- Mantiene historial de versiones y cambios.
- Facilita la revisión del código sin descargar archivos.
- Permite complementar el repositorio con documentación Markdown.
- Puede alojar un sitio estático mediante GitHub Pages, adecuado para este portafolio.

## 5. Buenas prácticas incorporadas

- README principal con perfil profesional y enlaces.
- README específico en cada proyecto.
- Estructura de carpetas consistente.
- Dependencias declaradas en un único archivo.
- Evidencias gráficas guardadas junto al proyecto correspondiente.
- Uso de nombres descriptivos sin sufijos de descargas duplicadas como `(1)`.
- Separación explícita entre trabajos propios y material de apoyo docente.
- Documentación de limitaciones: el clasificador de sentimiento depende de un archivo `comentarios_clientes.xlsx` que no fue incluido entre los archivos suministrados para esta entrega.

## 6. Mejoras aplicadas al consolidar los trabajos

Durante la preparación del portafolio se aplicaron mejoras de presentación y revisión técnica:

- Se normalizaron nombres de archivos para mejorar navegación y lectura.
- Se verificó la ejecución local de los trabajos de inferencia estadística, aprendizaje no supervisado y perceptrón.
- Se conservaron los resultados gráficos generados por los scripts validados.
- Se documentó el requisito externo del proyecto de sentimiento en lugar de ocultar o inventar el dataset faltante.
- En el trabajo no supervisado se mantiene la selección de `k` mediante Silhouette Score, evitando fijar un valor arbitrario.
- En el clasificador de sentimiento se conserva la práctica de ajustar el tokenizer solo con el conjunto de entrenamiento, reduciendo riesgo de fuga de datos.
- Se agregó un sitio estático para que el contenido pueda alojarse mediante GitHub Pages.

## 7. Estrategia de hosting

El portafolio se prepara como sitio web estático (`index.html` + `assets/styles.css`), por lo que puede publicarse con **GitHub Pages** desde la rama `main` y la carpeta raíz. Esta modalidad es adecuada porque no requiere backend ni procesamiento en servidor.
