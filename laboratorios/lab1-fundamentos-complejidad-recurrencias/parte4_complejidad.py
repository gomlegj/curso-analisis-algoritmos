"""Parte 4: insertion sort contra merge sort sobre el escenario A.

Mide el tiempo de los dos algoritmos con los mismos tamaños de la Parte 3
y guarda la gráfica comparativa en graficas/parte4_tiempo.png.

Uso (desde la raíz del repositorio, con el entorno virtual activo):
    python laboratorios/lab1-fundamentos-complejidad-recurrencias/parte4_complejidad.py
"""

import statistics
import time
from pathlib import Path
from typing import Callable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
SEMILLA = 42
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

# Tamaños extra, más pequeños que los de la Parte 3, para ver en qué
# punto merge sort empieza a ganar.
TAMANOS_PEQUENOS = [5, 10, 20, 40, 60, 80, 100]
REPETICIONES_PEQUENOS = 2000

ALGORITMOS: dict[str, Callable[[list[int]], tuple[list[int], int]]] = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
}


def medir_algoritmo(
    algoritmo: Callable[[list[int]], tuple[list[int], int]],
) -> tuple[list[float], list[int]]:
    """Mide un algoritmo sobre el escenario A para todos los tamaños.

    Args:
        algoritmo: función de ordenamiento instrumentada de algoritmos.py.

    Returns:
        Una tupla con los tiempos (mediana de REPETICIONES corridas, en
        segundos) y las comparaciones, en el mismo orden que TAMANOS.
    """
    tiempos: list[float] = []
    comparaciones: list[int] = []

    for n in TAMANOS:
        # Los dos algoritmos reciben exactamente el mismo lote (misma
        # semilla); si no, la comparación no sería justa.
        lote = generar_aleatorio(n, SEMILLA)
        corridas: list[float] = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            _, comps = algoritmo(lote)
            corridas.append(time.perf_counter() - inicio)
        tiempos.append(statistics.median(corridas))
        comparaciones.append(comps)

    return tiempos, comparaciones


def medir_tamanos_pequenos() -> None:
    """Compara los dos algoritmos con listas muy pequeñas e imprime la tabla.

    Con tan pocos elementos una corrida dura microsegundos y el ruido se
    come el resultado, por eso cada medición se repite
    REPETICIONES_PEQUENOS veces y se toma la mediana.
    """
    print(f"\nTamaños pequeños (mediana de {REPETICIONES_PEQUENOS} corridas, en microsegundos)")
    print(f"{'n':>6} | {'insertion (us)':>14} | {'merge (us)':>10}")
    print("-" * 38)
    for n in TAMANOS_PEQUENOS:
        lote = generar_aleatorio(n, SEMILLA)
        medianas: dict[str, float] = {}
        for nombre, algoritmo in ALGORITMOS.items():
            corridas: list[float] = []
            for _ in range(REPETICIONES_PEQUENOS):
                inicio = time.perf_counter()
                algoritmo(lote)
                corridas.append(time.perf_counter() - inicio)
            medianas[nombre] = statistics.median(corridas) * 1e6
        print(
            f"{n:>6} | {medianas['Insertion sort']:>14.1f} "
            f"| {medianas['Merge sort']:>10.1f}"
        )


def graficar(tiempos: dict[str, list[float]]) -> None:
    """Dibuja tiempo vs. n con una curva por algoritmo y la guarda.

    Args:
        tiempos: diccionario algoritmo -> tiempos medidos por tamaño.
    """
    estilos = {"Insertion sort": ("o", "crimson"), "Merge sort": ("s", "dodgerblue")}
    plt.figure(figsize=(9, 5.5))
    for nombre, valores in tiempos.items():
        marcador, color = estilos[nombre]
        plt.plot(TAMANOS, valores, marker=marcador, color=color, label=nombre)
    plt.title(
        "Tamiza, escenario A (aleatorio): tiempo vs. tamaño de entrada\n"
        f"(mediana de {REPETICIONES} corridas)"
    )
    plt.xlabel("Tamaño de entrada n (número de registros)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend(title="Algoritmo")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte4_tiempo.png", dpi=120)
    plt.close()


def main() -> None:
    """Corre la medición comparativa de la Parte 4 e imprime la tabla."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    tiempos: dict[str, list[float]] = {}
    comparaciones: dict[str, list[int]] = {}
    for nombre, algoritmo in ALGORITMOS.items():
        print(f"Midiendo {nombre}...")
        tiempos[nombre], comparaciones[nombre] = medir_algoritmo(algoritmo)

    print(
        f"\n{'n':>6} | {'insertion (s)':>13} | {'merge (s)':>10} | "
        f"{'comp. insertion':>15} | {'comp. merge':>11}"
    )
    print("-" * 68)
    for i, n in enumerate(TAMANOS):
        print(
            f"{n:>6} | {tiempos['Insertion sort'][i]:>13.5f} "
            f"| {tiempos['Merge sort'][i]:>10.5f} "
            f"| {comparaciones['Insertion sort'][i]:>15,} "
            f"| {comparaciones['Merge sort'][i]:>11,}"
        )

    medir_tamanos_pequenos()

    graficar(tiempos)
    print(f"\nGráfica guardada en {CARPETA_GRAFICAS / 'parte4_tiempo.png'}")


if __name__ == "__main__":
    main()
