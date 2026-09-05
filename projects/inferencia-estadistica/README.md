# Inferencia estadística

## Objetivo

Analizar una muestra simulada de 200 estudiantes y aplicar herramientas de estadística descriptiva e inferencial para evaluar el puntaje de satisfacción.

## Qué realiza el script

1. Genera un dataset reproducible.
2. Explora variables y detecta valores nulos.
3. Imputa valores faltantes con criterios documentados.
4. Calcula media, varianza, asimetría y Shapiro-Wilk.
5. Genera un histograma.
6. Calcula un intervalo de confianza del 95% para la media.
7. Realiza una prueba t bilateral contra el valor de referencia 7.
8. Entrega una reflexión final.

## Resultado de validación

En la ejecución revisada para este portafolio:

- Media muestral de satisfacción: **7.180**.
- IC 95%: **[7.007, 7.354]**.
- Prueba t: **p = 0.041699**.
- Con `α = 0.05`, se rechaza H0 y la media observada resulta significativamente distinta de 7.

## Ejecución

```bash
python desafio_inferencia_estadistica.py
```

El script genera `histograma_satisfaccion_gabriela_duran.png` en la misma carpeta.
