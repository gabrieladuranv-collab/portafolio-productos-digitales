# -*- coding: utf-8 -*-
"""
Desafío: Inferencia estadística
Autora: Gabriela Durán Vidal

Este programa:
1. Simula un DataFrame con 200 estudiantes.
2. Realiza análisis descriptivo y tratamiento de valores nulos.
3. Grafica la distribución de los puntajes de satisfacción.
4. Calcula un intervalo de confianza del 95%.
5. Realiza una prueba t de una muestra para contrastar si la media es igual a 7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


def crear_datos(cantidad: int = 200, semilla: int = 42) -> pd.DataFrame:
    """Crea un DataFrame reproducible con información de estudiantes."""
    rng = np.random.default_rng(semilla)

    edades = np.clip(
        np.rint(rng.normal(loc=29, scale=8, size=cantidad)),
        18,
        60,
    ).astype(float)

    generos = rng.choice(
        ["Mujer", "Hombre", "No binario", "Prefiere no responder"],
        size=cantidad,
        p=[0.48, 0.44, 0.05, 0.03],
    ).astype(object)

    puntajes_satisfaccion = np.clip(
        rng.normal(loc=7.25, scale=1.25, size=cantidad),
        1,
        10,
    ).round(2)

    horas_estudio = np.clip(
        rng.normal(loc=8.5, scale=3.0, size=cantidad),
        1,
        20,
    ).round(1)

    df = pd.DataFrame(
        {
            "Edad": edades,
            "Genero": generos,
            "Puntaje_satisfaccion": puntajes_satisfaccion,
            "Horas_estudio_semanales": horas_estudio,
        }
    )

    indices_edad = rng.choice(df.index, size=3, replace=False)
    indices_genero = rng.choice(df.index, size=2, replace=False)
    indices_horas = rng.choice(df.index, size=4, replace=False)

    df.loc[indices_edad, "Edad"] = np.nan
    df.loc[indices_genero, "Genero"] = np.nan
    df.loc[indices_horas, "Horas_estudio_semanales"] = np.nan

    return df


def mostrar_titulo(texto: str) -> None:
    print("\n" + "=" * 78)
    print(texto)
    print("=" * 78)


def explorar_y_tratar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    mostrar_titulo("1. CARGA Y EXPLORACIÓN DE DATOS")

    print(f"Cantidad de registros: {df.shape[0]}")
    print(f"Cantidad de variables: {df.shape[1]}")
    print("\nPrimeros cinco registros:")
    print(df.head().to_string(index=False))

    columnas_numericas = ["Edad", "Puntaje_satisfaccion", "Horas_estudio_semanales"]
    estadisticas = (
        df[columnas_numericas]
        .agg(["mean", "median", "std"])
        .T
        .rename(columns={"mean": "Media", "median": "Mediana", "std": "Desviacion_estandar"})
    )

    print("\nEstadísticas descriptivas de las variables numéricas:")
    print(estadisticas.round(2).to_string())

    print("\nValores nulos detectados por variable:")
    print(df.isna().sum().to_string())

    print(
        "\nTratamiento aplicado:\n"
        "- Edad y horas de estudio: se reemplazan los valores nulos por la mediana, "
        "porque es una medida robusta frente a valores extremos.\n"
        "- Género: se reemplaza por la categoría más frecuente (moda).\n"
        "- Puntaje de satisfacción: no presenta nulos."
    )

    df_limpio = df.copy()
    for columna in ["Edad", "Horas_estudio_semanales"]:
        df_limpio[columna] = df_limpio[columna].fillna(df_limpio[columna].median())

    moda_genero = df_limpio["Genero"].mode(dropna=True)[0]
    df_limpio["Genero"] = df_limpio["Genero"].fillna(moda_genero)

    print("\nValores nulos después del tratamiento:")
    print(df_limpio.isna().sum().to_string())
    return df_limpio


def analizar_distribucion(df: pd.DataFrame, carpeta_salida: Path) -> None:
    mostrar_titulo("2. DISTRIBUCIÓN Y VISUALIZACIÓN")
    puntajes = df["Puntaje_satisfaccion"].to_numpy()

    media_numpy = np.mean(puntajes)
    varianza_numpy = np.var(puntajes, ddof=1)
    asimetria = stats.skew(puntajes, bias=False)
    estadistico_shapiro, p_shapiro = stats.shapiro(puntajes)

    print(f"Media del puntaje de satisfacción: {media_numpy:.3f}")
    print(f"Varianza muestral del puntaje de satisfacción: {varianza_numpy:.3f}")
    print(f"Asimetría: {asimetria:.3f}")
    print(f"Prueba de Shapiro-Wilk: W = {estadistico_shapiro:.4f}")
    print(f"Valor-p de Shapiro-Wilk: {p_shapiro:.4f}")

    if p_shapiro >= 0.05 and abs(asimetria) < 0.5:
        interpretacion = (
            "La distribución parece aproximadamente normal: presenta poca asimetría "
            "y la prueba de Shapiro-Wilk no entrega evidencia suficiente para rechazar "
            "la normalidad al nivel de significancia de 0,05."
        )
    else:
        interpretacion = (
            "La distribución no parece completamente normal. El histograma, la "
            "asimetría o la prueba de Shapiro-Wilk muestran diferencias respecto "
            "de una distribución normal."
        )

    print("\nInterpretación:")
    print(interpretacion)

    plt.figure(figsize=(9, 5))
    plt.hist(puntajes, bins=12, edgecolor="black")
    plt.axvline(media_numpy, linestyle="--", linewidth=2, label=f"Media = {media_numpy:.2f}")
    plt.title("Distribución de los puntajes de satisfacción")
    plt.xlabel("Puntaje de satisfacción")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.tight_layout()

    ruta_histograma = carpeta_salida / "histograma_satisfaccion_gabriela_duran.png"
    plt.savefig(ruta_histograma, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"\nHistograma guardado en: {ruta_histograma}")


def calcular_intervalo_confianza(df: pd.DataFrame) -> tuple[float, float]:
    mostrar_titulo("3. INTERVALO DE CONFIANZA DEL 95%")
    puntajes = df["Puntaje_satisfaccion"].dropna().to_numpy()
    n = len(puntajes)
    media = np.mean(puntajes)
    desviacion = np.std(puntajes, ddof=1)
    error_estandar = desviacion / np.sqrt(n)
    grados_libertad = n - 1
    valor_t_critico = stats.t.ppf(0.975, df=grados_libertad)
    margen_error = valor_t_critico * error_estandar

    limite_inferior = media - margen_error
    limite_superior = media + margen_error

    print(f"Tamaño de la muestra: {n}")
    print(f"Media muestral: {media:.3f}")
    print(f"Error estándar: {error_estandar:.4f}")
    print(f"Valor t crítico: {valor_t_critico:.4f}")
    print(f"Intervalo de confianza del 95%: [{limite_inferior:.3f}, {limite_superior:.3f}]")
    print(
        "\nInterpretación:\n"
        "Con un 95% de confianza, se estima que la media real del puntaje de "
        f"satisfacción de todos los estudiantes del curso se encuentra entre "
        f"{limite_inferior:.2f} y {limite_superior:.2f} puntos."
    )
    return limite_inferior, limite_superior


def realizar_prueba_hipotesis(df: pd.DataFrame) -> None:
    mostrar_titulo("4. PRUEBA DE HIPÓTESIS")
    puntajes = df["Puntaje_satisfaccion"].dropna().to_numpy()
    media_muestral = np.mean(puntajes)
    valor_referencia = 7
    alpha = 0.05

    estadistico_t, valor_p = stats.ttest_1samp(puntajes, popmean=valor_referencia)

    print("Hipótesis nula (H0): la media poblacional de satisfacción es igual a 7.")
    print("Hipótesis alternativa (H1): la media poblacional de satisfacción es distinta de 7.")
    print(f"Nivel de significancia: {alpha}")
    print(f"Media muestral observada: {media_muestral:.3f}")
    print(f"Estadístico t: {estadistico_t:.4f}")
    print(f"Valor-p: {valor_p:.6f}")

    if valor_p < alpha:
        direccion = "superior" if media_muestral > valor_referencia else "inferior"
        print("\nDecisión estadística: se rechaza H0, porque el valor-p es menor que 0,05.")
        print(
            "Conclusión práctica: existe evidencia estadísticamente significativa "
            f"de que el promedio de satisfacción es diferente de 7 y, en esta muestra, es {direccion}."
        )
    else:
        print("\nDecisión estadística: no se rechaza H0, porque el valor-p es mayor o igual que 0,05.")
        print("Conclusión práctica: la muestra no entrega evidencia suficiente para afirmar que el promedio sea distinto de 7.")


def mostrar_reflexion_final() -> None:
    mostrar_titulo("5. REFLEXIÓN FINAL")
    print(
        "La estadística inferencial permite usar una muestra para estimar y contrastar\n"
        "características de una población. Sus intervalos y pruebas cuantifican la\n"
        "incertidumbre, evitando decisiones basadas solo en impresiones. En la empresa,\n"
        "esto ayuda a evaluar resultados, detectar diferencias relevantes y decidir\n"
        "con evidencia, considerando siempre la calidad y representatividad de los datos."
    )


def main() -> None:
    carpeta_salida = Path(__file__).resolve().parent
    print("DESAFÍO DE INFERENCIA ESTADÍSTICA")
    print("Autora: Gabriela Durán Vidal")
    datos = crear_datos(cantidad=200, semilla=42)
    datos_limpios = explorar_y_tratar_nulos(datos)
    analizar_distribucion(datos_limpios, carpeta_salida)
    calcular_intervalo_confianza(datos_limpios)
    realizar_prueba_hipotesis(datos_limpios)
    mostrar_reflexion_final()


if __name__ == "__main__":
    main()
