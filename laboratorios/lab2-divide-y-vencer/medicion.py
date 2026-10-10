"""Script de medición de tiempos de ejecución y generación de gráfica."""

import os
import random
import time
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_rendimiento() -> None:
    tamanios = [10, 50, 100, 500, 1000, 4000, 8000]
    tiempos_fb = []
    tiempos_dv = []

    # Semilla fija para reproducibilidad
    random.seed(123)
    repeticiones = 3

    print(f"{'Tamaño (n)':<12} | {'Fuerza Bruta (s)':<18} | {'Divide y Vencerás (s)':<22}")
    print("-" * 58)

    for n in tamanios:
        # Generar lista con valores enteros entre -100 y 100
        serie = [random.randint(-100, 100) for _ in range(n)]

        # Validar en cada tamaño que ambos devuelven la misma suma
        res_fb_val = subarreglo_fuerza_bruta(serie)[2]
        res_dv_val = subarreglo_maximo(serie, 0, len(serie) - 1)[2]
        assert res_fb_val == res_dv_val, f"Discrepancia en tamaño {n}"

        # Medición para Fuerza Bruta (promedio de repeticiones para mitigar ruido)
        t_fb_acum = 0.0
        for _ in range(repeticiones):
            inicio_t = time.perf_counter()
            subarreglo_fuerza_bruta(serie)
            t_fb_acum += time.perf_counter() - inicio_t
        t_fb_prom = t_fb_acum / repeticiones
        tiempos_fb.append(t_fb_prom)

        # Medición para Divide y Vencerás
        t_dv_acum = 0.0
        for _ in range(repeticiones):
            inicio_t = time.perf_counter()
            subarreglo_maximo(serie, 0, len(serie) - 1)
            t_dv_acum += time.perf_counter() - inicio_t
        t_dv_prom = t_dv_acum / repeticiones
        tiempos_dv.append(t_dv_prom)

        print(f"{n:<12} | {t_fb_prom:<18.6f} | {t_dv_prom:<22.6f}")

    # Generación y almacenamiento de la gráfica
    os.makedirs("graficas", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos_fb, marker='o', label='Fuerza Bruta $\\Theta(n^2)$', color='crimson')
    plt.plot(tamanios, tiempos_dv, marker='s', label='Divide y Vencerás $\\Theta(n \\log n)$', color='dodgerblue')

    plt.title('Comparación de Tiempos de Ejecución: Subarreglo Máximo', fontsize=14, fontweight='bold')
    plt.xlabel('Tamaño de entrada ($n$ días)', fontsize=12)
    plt.ylabel('Tiempo de ejecución promedio (segundos)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()

    ruta_grafica = os.path.join('graficas', 'tiempo_vs_n.png')
    plt.savefig(ruta_grafica, dpi=300)
    plt.close()
    print(f"\nGráfica guardada exitosamente en: {ruta_grafica}")


if __name__ == "__main__":
    medir_rendimiento()