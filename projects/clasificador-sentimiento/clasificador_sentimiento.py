"""
Clasificador de sentimiento de comentarios de clientes - Deep Learning con Keras
Desafío: Aplicaciones reales del Deep Learning

Caso de uso: una empresa de análisis predictivo necesita identificar automáticamente
qué comentarios de clientes en redes sociales tienen tono negativo, para priorizar
la respuesta del equipo de atención.

Dataset: comentarios_clientes.xlsx (columnas: comentario, sentimiento [0=negativo, 1=positivo])

Ejecutar con: python clasificador_sentimiento.py
"""

import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, GlobalAveragePooling1D, Dense, Dropout
from sklearn.model_selection import train_test_split

# 1. Carga de datos
df = pd.read_excel("comentarios_clientes.xlsx")
print("Dimensiones del dataset:", df.shape)
print(df["sentimiento"].value_counts())

comentarios = df["comentario"].astype(str).values
etiquetas = df["sentimiento"].values

# 2. Split entrenamiento / prueba
X_train_text, X_test_text, y_train, y_test = train_test_split(
    comentarios, etiquetas, test_size=0.2, random_state=42, stratify=etiquetas
)

# 3. Preprocesamiento: tokenización y padding
VOCAB_SIZE = 1000
MAX_LEN = 12
OOV_TOKEN = "<OOV>"

tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token=OOV_TOKEN)
# Se ajusta el tokenizer SOLO con el set de entrenamiento para evitar fuga de datos.
tokenizer.fit_on_texts(X_train_text)

X_train_seq = tokenizer.texts_to_sequences(X_train_text)
X_test_seq = tokenizer.texts_to_sequences(X_test_text)

X_train_pad = pad_sequences(X_train_seq, maxlen=MAX_LEN, padding="post", truncating="post")
X_test_pad = pad_sequences(X_test_seq, maxlen=MAX_LEN, padding="post", truncating="post")

print("Tamaño real del vocabulario encontrado:", len(tokenizer.word_index))
print("Ejemplo de comentario tokenizado y padded:")
print(X_train_text[0], "->", X_train_pad[0])

# 4. Construcción del modelo
EMBEDDING_DIM = 16

modelo = Sequential([
    Input(shape=(MAX_LEN,)),
    Embedding(input_dim=VOCAB_SIZE, output_dim=EMBEDDING_DIM),
    GlobalAveragePooling1D(),
    Dense(16, activation="relu"),
    Dropout(0.3),
    Dense(1, activation="sigmoid"),
])

modelo.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
modelo.summary()

# 5. Entrenamiento
historial = modelo.fit(
    X_train_pad, y_train,
    epochs=15,
    batch_size=16,
    validation_split=0.2,
    verbose=2,
)

# 6. Evaluación
loss, accuracy = modelo.evaluate(X_test_pad, y_test, verbose=0)
print(f"\nExactitud (accuracy) en el set de prueba: {accuracy:.4f}")
print(f"Pérdida (loss) en el set de prueba: {loss:.4f}")

# 7. Prueba con comentarios nuevos
comentarios_nuevos = [
    "El producto llegó roto y nadie responde mis mensajes",
    "Quedé muy conforme con la rapidez de la entrega",
]
seq_nuevos = tokenizer.texts_to_sequences(comentarios_nuevos)
pad_nuevos = pad_sequences(seq_nuevos, maxlen=MAX_LEN, padding="post", truncating="post")
predicciones = modelo.predict(pad_nuevos, verbose=0)

print("\n=== Predicciones sobre comentarios nuevos ===")
for texto, pred in zip(comentarios_nuevos, predicciones):
    etiqueta = "POSITIVO" if pred[0] >= 0.5 else "NEGATIVO"
    print(f"'{texto}' -> {etiqueta} (probabilidad positivo: {pred[0]:.3f})")

# 8. Gráfico de curvas de entrenamiento
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(historial.history["accuracy"], label="Entrenamiento")
axes[0].plot(historial.history["val_accuracy"], label="Validación", linestyle="--")
axes[0].set_title("Exactitud (accuracy) por época")
axes[0].set_xlabel("Época")
axes[0].set_ylabel("Accuracy")
axes[0].legend()

axes[1].plot(historial.history["loss"], label="Entrenamiento")
axes[1].plot(historial.history["val_loss"], label="Validación", linestyle="--")
axes[1].set_title("Pérdida (loss) por época")
axes[1].set_xlabel("Época")
axes[1].set_ylabel("Loss")
axes[1].legend()

plt.tight_layout()
plt.savefig("curvas_entrenamiento.png", dpi=200, facecolor="white")
print("\nGráfico de curvas guardado en curvas_entrenamiento.png")
