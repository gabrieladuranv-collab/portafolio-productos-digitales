# Exploración con aprendizaje no supervisado

## Objetivo

Explorar un pequeño dataset de egresados sin variable objetivo, aplicar clustering y reducción de dimensionalidad para detectar perfiles naturales.

## Metodología

- Estandarización de variables numéricas con `StandardScaler`.
- Codificación de `Interes_formativo` con `OneHotEncoder`.
- Evaluación de `k = 2, 3, 4` mediante **Silhouette Score**.
- Ajuste de K-means con el mejor `k`.
- Reducción a dos componentes con **PCA**.
- Visualización y resumen de perfiles por cluster.

## Resultado de validación

- Mejor valor: **k = 2**.
- Silhouette Score para k=2: **0.2967**.
- Varianza total explicada por las dos componentes PCA: **89.34%**.

La segmentación separa principalmente un grupo de egresados más jóvenes con menos cursos aprobados de otro grupo de mayor edad con más cursos aprobados.

## Ejecución

```bash
python desafio_exploracion_unsupervised.py
```

El script genera `clusters_pca.png`.
