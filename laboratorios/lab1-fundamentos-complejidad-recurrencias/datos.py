"""Generadores de lotes de registros para los escenarios de Tamiza.

El índice de riesgo va de 0 a 1000, pero con solo 1001 enteros posibles
no alcanzaría para lotes de 6400 registros distintos. Por eso los índices
van en milésimas de punto: 734.215 se guarda como el entero 734215 y el
rango queda de 0 a 1.000.000.

Criterio de orden: el algoritmo produce la lista de MAYOR a MENOR riesgo.
"""

import random

# 1000 puntos de riesgo expresados en milésimas.
INDICE_MAXIMO = 1_000_000

# En el escenario B, el 2 % del lote son resultados nuevos del día.
FRACCION_NUEVOS = 0.02


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    # Un Random propio evita que otra parte del programa cambie la semilla.
    generador = random.Random(semilla)
    # sample no repite valores y los entrega revueltos, parecido a como
    # quedan los registros cuando cada laboratorio sube los suyos.
    return generador.sample(range(INDICE_MAXIMO + 1), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    generador = random.Random(semilla)
    indices = generador.sample(range(INDICE_MAXIMO + 1), n)

    cantidad_nuevos = round(n * FRACCION_NUEVOS)
    cantidad_ayer = n - cantidad_nuevos

    # La lista de ayer debe quedar de mayor a menor sin usar funciones de
    # ordenamiento de Python. El truco: recorrer todos los índices posibles
    # de arriba hacia abajo y quedarme con los que están en el lote de ayer;
    # así salen en orden sin tener que comparar unos con otros.
    de_ayer = set(indices[:cantidad_ayer])
    lista_ayer = [v for v in range(INDICE_MAXIMO, -1, -1) if v in de_ayer]

    # Al final se pegan los nuevos, tal como llegaron.
    nuevos = indices[cantidad_ayer:]
    return lista_ayer + nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    # El sistema legado exporta de menor a mayor riesgo, justo al revés.
    # Con un paso fijo los índices quedan repartidos y no se repiten.
    paso = max(1, INDICE_MAXIMO // n)
    return [i * paso for i in range(n)]
