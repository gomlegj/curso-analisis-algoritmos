"""Parte 3: peor, mejor y caso promedio de insertion sort en Tamiza.

Corre insertion sort sobre los tres escenarios de entrada (A aleatorio,
B casi ordenado, C inverso), mide tiempo y comparaciones y guarda las dos
gráficas de la parte en graficas/.

Uso (desde la raíz del repositorio, con el entorno virtual activo):
    python laboratorios/lab1-fundamentos-complejidad-recurrencias/parte3_casos.py
"""

import statistics
import time
from pathlib import Path
from typing import Callable

import matplotlib

matplotlib.use("Agg")  # las gráficas van directo a PNG, sin abrir ventanas
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
SEMILLA = 42
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

# A y B necesitan semilla y C no; con las lambdas los tres se llaman
# igual, generador(n), y el ciclo de medición no tiene que distinguirlos.
ESCENARIOS: dict[str, Callable[[int], list[int]]] = {
    "A — Aleatorio": lambda n: generar_aleatorio(n, SEMILLA),
    "B — Casi ordenado": lambda n: generar_casi_ordenado(n, SEMILLA),
    "C — Orden inverso": generar_inverso,
}


def medir_escenario(
    generador: Callable[[int], list[int]],
) -> tuple[list[float], list[int]]:
    """Mide insertion sort sobre un escenario para todos los tamaños.

    Args:
        generador: función que recibe n y devuelve el lote a ordenar.

    Returns:
        Una tupla con la lista de tiempos (mediana de REPETICIONES
        corridas, en segundos) y la lista de comparaciones, en el mismo
        orden que TAMANOS.
    """
    tiempos: list[float] = []
    comparaciones: list[int] = []

    for n in TAMANOS:
        # La generación del lote queda por fuera del cronómetro.
        lote = generador(n)
        corridas: list[float] = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            _, comps = insertion_sort(lote)
            corridas.append(time.perf_counter() - inicio)
        # Con la mediana, un pico del sistema operativo en una corrida no
        # daña el dato. Las comparaciones dan igual en las tres corridas
        # porque el lote no cambia.
        tiempos.append(statistics.median(corridas))
        comparaciones.append(comps)

    return tiempos, comparaciones


def graficar(
    resultados: dict[str, list[float]] | dict[str, list[int]],
    titulo: str,
    etiqueta_y: str,
    archivo: str,
) -> None:
    """Dibuja una curva por escenario en los mismos ejes y la guarda.

    Args:
        resultados: diccionario escenario -> valores medidos por tamaño.
        titulo: título de la gráfica.
        etiqueta_y: rótulo del eje vertical (con unidades).
        archivo: nombre del archivo PNG dentro de graficas/.
    """
    marcadores = {"A": "o", "B": "s", "C": "^"}
    plt.figure(figsize=(9, 5.5))
    for nombre, valores in resultados.items():
        plt.plot(TAMANOS, valores, marker=marcadores[nombre[0]], label=nombre)
    plt.title(titulo)
    plt.xlabel("Tamaño de entrada n (número de registros)")
    plt.ylabel(etiqueta_y)
    plt.legend(title="Escenario de Tamiza")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / archivo, dpi=120)
    plt.close()


def main() -> None:
    """Corre el experimento de la Parte 3 e imprime la tabla de resultados."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    # Antes de medir, un chequeo del contador: si la lista ya viene de
    # mayor a menor, insertion sort tiene que hacer justo n - 1 comparaciones.
    ya_ordenada = list(range(100, 0, -1))
    assert insertion_sort(ya_ordenada)[1] == 99, "conteo de comparaciones mal"

    tiempos: dict[str, list[float]] = {}
    comparaciones: dict[str, list[int]] = {}
    for nombre, generador in ESCENARIOS.items():
        print(f"Midiendo escenario {nombre}...")
        tiempos[nombre], comparaciones[nombre] = medir_escenario(generador)

    print(f"\n{'n':>6} | {'escenario':<18} | {'comparaciones':>13} | {'tiempo (s)':>10}")
    print("-" * 58)
    for i, n in enumerate(TAMANOS):
        for nombre in ESCENARIOS:
            print(
                f"{n:>6} | {nombre:<18} | {comparaciones[nombre][i]:>13,} "
                f"| {tiempos[nombre][i]:>10.5f}"
            )

    graficar(
        comparaciones,
        "Insertion sort: comparaciones vs. tamaño de entrada",
        "Comparaciones entre elementos",
        "parte3_comparaciones.png",
    )
    graficar(
        tiempos,
        f"Insertion sort: tiempo vs. tamaño de entrada (mediana de {REPETICIONES})",
        "Tiempo de ejecución (segundos)",
        "parte3_tiempo.png",
    )
    print(f"\nGráficas guardadas en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
