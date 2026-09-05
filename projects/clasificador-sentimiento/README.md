# Clasificador de sentimiento con Deep Learning

## Caso de uso

Clasificar automáticamente comentarios de clientes como negativos (`0`) o positivos (`1`) para priorizar respuestas del equipo de atención.

## Arquitectura

- Tokenización de texto.
- Padding de secuencias.
- `Embedding`.
- `GlobalAveragePooling1D`.
- Capa densa con ReLU.
- `Dropout`.
- Salida sigmoide para clasificación binaria.
- Entrenamiento con Adam y `binary_crossentropy`.

## Buena práctica destacada

El tokenizer se ajusta **solo con el conjunto de entrenamiento**, evitando incorporar información del set de prueba durante el preprocesamiento.

## Dependencia de datos

El código original espera un archivo:

```text
comentarios_clientes.xlsx
```

con las columnas:

```text
comentario
sentimiento
```

Ese dataset no fue incluido entre los archivos suministrados para consolidar este portafolio, por lo que se conserva la dependencia explícita en vez de sustituirla por datos inventados.

## Ejecución

```bash
python clasificador_sentimiento.py
```

Requiere TensorFlow/Keras y `openpyxl` además del dataset indicado.
