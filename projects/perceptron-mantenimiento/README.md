# Perceptrón — alerta de mantenimiento predictivo

## Caso de uso

Una empresa de logística monitorea vehículos con dos variables normalizadas:

- `x1`: vibración del motor.
- `x2`: temperatura del motor.

El perceptrón produce una salida binaria:

- `1`: generar alerta de mantenimiento preventivo.
- `0`: operación normal.

## Qué demuestra

- Inicialización de pesos y sesgo.
- Suma ponderada.
- Función de activación escalón.
- Regla de actualización del perceptrón.
- Entrenamiento por épocas hasta convergencia.
- Predicción sobre un caso nuevo.

## Resultado de validación

El modelo alcanzó convergencia en la **época 4**, clasificó correctamente el set de entrenamiento y, para el vehículo `[0.78, 0.82]`, generó una **alerta de mantenimiento**.

## Ejecución

```bash
python perceptron_alerta_mantenimiento.py
```
