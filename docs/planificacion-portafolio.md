# Planificación del portafolio digital

## 1. Continuidad del trabajo

Este portafolio da continuidad al trabajo de planificación desarrollado previamente para el **Portafolio virtual**. En esa etapa se definió el uso de un repositorio, la selección de trabajos representativos, la construcción de un perfil profesional y la incorporación de buenas prácticas para presentar los proyectos de forma clara y accesible.

Para esta versión se mantienen los mismos criterios y se consolidan los trabajos utilizados durante el proceso de formación, incorporando mejoras de organización, documentación y reproducibilidad.

## 2. Propósito

Construir un repositorio profesional que concentre trabajos realizados durante la formación y permita a docentes, empresas o reclutadores revisar rápidamente evidencia de habilidades técnicas, capacidad de análisis y documentación.

## 3. Repositorio seleccionado: GitHub

Se mantiene **GitHub** como repositorio principal por las siguientes razones:

- Es una plataforma ampliamente utilizada en desarrollo de software y análisis de datos.
- Permite compartir el trabajo mediante un enlace único y público.
- Mantiene historial de versiones y cambios.
- Facilita la revisión del código sin necesidad de descargar todos los archivos.
- Permite organizar distintos proyectos mediante carpetas y archivos README.
- Admite documentación en Markdown.
- Permite complementar el repositorio con un sitio estático mediante GitHub Pages.

## 4. Público objetivo

- Docentes que revisan los trabajos desarrollados durante la formación.
- Reclutadores/as y equipos TI o de datos.
- Personas interesadas en proyectos de People Analytics, analítica e inteligencia artificial aplicada.

## 5. Trabajo seleccionado como muestra principal

Se mantiene **Inferencia estadística** como uno de los trabajos centrales del portafolio porque permite mostrar distintas habilidades dentro de un mismo ejercicio:

- creación y análisis de datos;
- revisión y tratamiento de valores nulos;
- estadística descriptiva;
- visualización de distribuciones;
- cálculo de un intervalo de confianza del 95%;
- aplicación e interpretación de una prueba t de una muestra.

Este trabajo se complementa con los demás proyectos incluidos en el repositorio, de modo que el portafolio muestre una evolución desde estadística aplicada hacia machine learning y redes neuronales.

## 6. Trabajos incorporados

### Inferencia estadística

Análisis estadístico aplicado a una muestra simulada de estudiantes. Incluye estadística descriptiva, tratamiento de valores nulos, visualización, intervalo de confianza y prueba de hipótesis.

### Aprendizaje no supervisado

Ejercicio de segmentación mediante K-means, selección del número de clusters mediante Silhouette Score y reducción de dimensionalidad con PCA.

### Perceptrón para mantenimiento preventivo

Modelo de clasificación binaria que utiliza variables de vibración y temperatura para generar una alerta de mantenimiento.

### Clasificador de sentimiento

Modelo de procesamiento de lenguaje natural con TensorFlow/Keras para clasificar comentarios de clientes. El proyecto documenta de forma explícita su dependencia de un dataset externo.

## 7. Perfil profesional

El repositorio incorpora un perfil visible desde el README principal con:

- nombre real;
- fotografía o avatar;
- presentación profesional;
- áreas de interés;
- enlaces a LinkedIn, GitHub y sitio profesional;
- correo electrónico de contacto.

La presentación busca conectar la experiencia profesional en psicología y gestión de personas con el desarrollo de competencias en análisis de datos, People Analytics e inteligencia artificial aplicada.

## 8. Características definidas para el repositorio

1. **Accesibilidad:** navegación directa desde un README principal.
2. **Orden:** una carpeta por proyecto, evitando archivos dispersos.
3. **Trazabilidad:** documentación del objetivo, metodología y resultados.
4. **Reproducibilidad:** dependencias declaradas y uso de semillas cuando corresponde.
5. **Legibilidad:** nombres de archivos claros, comentarios en el código y secciones coherentes.
6. **Seguridad básica:** `.gitignore` para evitar publicar secretos, entornos virtuales o archivos temporales.
7. **Portabilidad:** instrucciones de instalación y ejecución con Python.
8. **Presentación profesional:** portada web estática preparada para GitHub Pages.

## 9. Buenas prácticas incorporadas

- README principal con perfil profesional y enlaces.
- README específico en cada proyecto.
- Estructura de carpetas consistente.
- Dependencias declaradas en un único archivo `requirements.txt`.
- Uso de `.gitignore` para archivos locales y temporales.
- Evidencias gráficas guardadas junto al proyecto correspondiente cuando existen.
- Uso de nombres descriptivos y consistentes.
- Uso de semillas aleatorias en los ejercicios que requieren reproducibilidad.
- Separación explícita entre trabajos propios y material de apoyo docente.
- Registro de dependencias o datos faltantes en lugar de inventar información.

## 10. Mejoras aplicadas al consolidar los trabajos

Durante la preparación del portafolio se aplicaron mejoras de presentación y revisión técnica:

- Se normalizaron nombres de archivos para mejorar navegación y lectura.
- Se verificó la ejecución local de los trabajos de inferencia estadística, aprendizaje no supervisado y perceptrón.
- Se documentaron los resultados y limitaciones de cada proyecto.
- En el trabajo no supervisado se mantiene la selección de `k` mediante Silhouette Score, evitando fijar un valor arbitrario.
- En el clasificador de sentimiento se conserva la práctica de ajustar el tokenizer solo con el conjunto de entrenamiento, reduciendo riesgo de fuga de datos.
- Se documentó el requisito externo del proyecto de sentimiento en lugar de ocultar o inventar el dataset faltante.
- Se agregó un sitio estático para complementar la navegación del repositorio.

## 11. Estrategia de hosting

El portafolio se prepara como sitio web estático mediante `index.html` y `assets/styles.css`, de modo que pueda publicarse mediante GitHub Pages desde la rama `main` y la carpeta raíz. Esta modalidad es adecuada porque el portafolio no requiere backend ni procesamiento en servidor.
