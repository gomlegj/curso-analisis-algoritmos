import math
import matplotlib.pyplot as plt


print("Hola mundo")

def trabajo_aproximado_a(n: int) -> float:
    """Calcula el trabajo aproximado a n.

    Args:
        n: número entero positivo.

    Returns:
        Valor aproximado del trabajo.
    """
    if n <= 0:
        raise ValueError("n debe ser un número entero positivo.")
    
    # Ejemplo de cálculo de trabajo aproximado
    trabajo = n**2
    return trabajo


def trabajo_aproximado_b(n: int) -> float:
    """Calcula el trabajo aproximado a n.

    Args:
        n: número entero positivo.

    Returns:
        Valor aproximado del trabajo.
    """
    if n <= 0:
        raise ValueError("n debe ser un número entero positivo.")
    
    # Ejemplo de cálculo de trabajo aproximado
    trabajo = n * math.log2(n)
    return trabajo


def graficar_y_comparar_algoritmos(tamanos: list[int], ruta_salida: str) -> None:
    """Grafica y compara los algoritmos de trabajo aproximado.

    Args:
        tamanos: lista de tamaños de entrada para evaluar los algoritmos.
        ruta_salida: ruta donde se guardará la imagen del gráfico.
    """
    trabajos_a = [trabajo_aproximado_a(n) for n in tamanos]
    trabajos_b = [trabajo_aproximado_b(n) for n in tamanos]

    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, trabajos_a, label='Trabajo Aproximado A (n^2)', marker='o')
    plt.plot(tamanos, trabajos_b, label='Trabajo Aproximado B (n log n)', marker='s')
    
    plt.title('Comparación de Algoritmos de Trabajo Aproximado')
    plt.xlabel('Tamaño de Entrada (n)')
    plt.ylabel('Valor del Trabajo Aproximado')
    plt.legend()
    plt.grid(True)
    plt.savefig(ruta_salida)
    plt.show()


if __name__ == "__main__":
        tamanos = [10, 100, 500, 1000, 5000, 10000, 30000]
        ruta_salida = "graficas/clase-1/comparacion_algoritmos.png"
        graficar_y_comparar_algoritmos(tamanos, ruta_salida)

def insertion_sort(arr: list[int]) -> list[int]:
    """Ordena una lista de enteros usando el algoritmo de ordenamiento por inserción.

    Args:
        arr: lista de enteros a ordenar.

    Returns:
        Lista ordenada de enteros.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
