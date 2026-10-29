"""Aqui medimos y graficamos el tiempo de busqueda en la lista y en la tabla hash."""

import gc
import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

# Guardo las gráficas junto al script, así funciona sin importar desde
# qué carpeta lo ejecuto
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"
ESTADOS = ("en bodega", "en reparto", "entregado", "devuelto")
TAMANOS = [100, 500, 1000, 5000, 20000, 50000]
N_FIJO = 20000
ALFAS = [0.25, 0.5, 1, 2, 4, 10]
BUSQUEDAS = 200
REPETICIONES = 15
MUESTRA_VERIFICACION = 100


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
       existentes: guias que ya estan almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_envios(n: int, semilla: int = 2026) -> list[tuple[int, str]]:
    """Genera n cantidad envios con guias distintas de diez digitos.

    Args:
        n: cantidad de envios a generar.
        semilla: semilla del generador, para reproducir la medicion.

     Returns:
        Una lista de parejas (guia, estado) sin guias repetidas.
    """
    azar = random.Random(semilla)
    # sample garantiza que las guías no se repitan.
    guias = azar.sample(range(10**9, 10**10), n)
    return [(guia, azar.choice(ESTADOS)) for guia in guias]


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo, probando divisores hasta su raiz.

    Args:
        numero: entero a revisar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: float) -> int:
    """Busca el primo mas cercano a un valor, alejandose de a uno.

    Args:
        objetivo: valor alrededor del cual se busca el primo.

    Returns:
        El primo mas cercano a `objetivo` (el menor si hay empate).
    """
    centro = max(2, round(objetivo))
    distancia = 0
    while True:
        if es_primo(centro - distancia):
            return centro - distancia
        if es_primo(centro + distancia):
            return centro + distancia
        distancia += 1


def construir(
    envios: list[tuple[int, str]], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye una lista y una tabla con los mismos envios.

    Args:
        envios: parejas (guia, estado) a insertar.
        m: numero de casillas de la tabla.

    Returns:
        La lista enlazada y la tabla hash ya llenas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia, estado in envios:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar(
    lista: ListaEnlazada, tabla: TablaHash, envios: list[tuple[int, str]]
) -> None:
    """Comprueba que lista y tabla devuelven el mismo estado.

    Args:
        lista: lista enlazada con los envios.
        tabla: tabla hash con los mismos envios.
        envios: parejas (guia, estado) insertadas en ambas.

    Raises:
        AssertionError: si alguna guia de la muestra no coincide.
    """
    azar = random.Random(99)
    muestra = azar.sample(envios, min(MUESTRA_VERIFICACION, len(envios)))
    for guia, estado in muestra:
        assert lista.buscar(guia) == tabla.buscar(guia) == estado


def tiempos_medios(
    casos: list[tuple[ListaEnlazada | TablaHash, list[int]]]
) -> list[float]:
    """Este metodo mide el tiempo medio por busqueda de varios casos, intercalados.

    Hago REPETICIONES rondas; en cada ronda busco una vez el lote de
    guias de cada caso. Asi, si el computador se pone lento un rato,
    eso afecta una sola ronda de cada caso y no todas las de uno. De
    cada caso me quedo con la ronda mas rapida: el ruido del sistema
    operativo solo puede sumar tiempo, asi que el minimo es el dato mas
    limpio. Solo cronometro las busquedas.

    Args:
        casos: parejas (estructura, guias a buscar en ella).

    Returns:
        El tiempo medio de una busqueda en cada caso, en segundos y en
        el mismo orden que `casos`.
    """
    mejores = [float("inf")] * len(casos)
    # Apago el recolector de basura mientras mido (igual que timeit),
    # porque una pausa suya pesa mucho frente a búsquedas de décimas de
    # microsegundo.
    gc.disable()
    try:
        for _ in range(REPETICIONES):
            for i, (estructura, guias) in enumerate(casos):
                inicio = time.perf_counter()
                for guia in guias:
                    estructura.buscar(guia)
                transcurrido = time.perf_counter() - inicio
                mejores[i] = min(mejores[i], transcurrido / len(guias))
    finally:
        gc.enable()
    return mejores


def experimento_a() -> tuple[list[float], list[float]]:
    """Mide lista frente a tabla para varios n, con alfa cercano a 2.

    Returns:
        Los tiempos medios por busqueda (en segundos) de la lista y de
        la tabla, en el mismo orden que TAMANOS.
    """
    casos: list[tuple[ListaEnlazada | TablaHash, list[int]]] = []
    casillas: list[int] = []
    for n in TAMANOS:
        envios = generar_envios(n)
        m = primo_cercano(n / 2)
        lista, tabla = construir(envios, m)
        verificar(lista, tabla, envios)
        # Uso las mismas guías inexistentes para las dos estructuras.
        inexistentes = generar_guias_inexistentes(
            {guia for guia, _ in envios}, BUSQUEDAS
        )
        casos += [(lista, inexistentes), (tabla, inexistentes)]
        casillas.append(m)

    tiempos = tiempos_medios(casos)
    # Los casos quedaron alternados: lista, tabla, lista, tabla...
    tiempos_lista = tiempos[0::2]
    tiempos_tabla = tiempos[1::2]

    print("Experimento A: busquedas de guias inexistentes")
    print(f"{'n':>7} {'m':>7} {'alfa':>6} {'lista (us)':>12} "
          f"{'tabla (us)':>12}")
    for n, m, t_lista, t_tabla in zip(TAMANOS, casillas, tiempos_lista,
                                      tiempos_tabla):
        print(f"{n:>7} {m:>7} {n / m:>6.2f} "
              f"{t_lista * 1e6:>12.2f} {t_tabla * 1e6:>12.3f}")
    return tiempos_lista, tiempos_tabla


def experimento_b() -> tuple[list[float], list[float]]:
    """Mide la tabla con n fijo para distintos factores de carga.

    Returns:
        Los factores de carga reales obtenidos y el tiempo medio por
        busqueda (en segundos) para cada uno.
    """
    envios = generar_envios(N_FIJO)
    existentes = {guia for guia, _ in envios}
    inexistentes = generar_guias_inexistentes(existentes, BUSQUEDAS)
    casos: list[tuple[ListaEnlazada | TablaHash, list[int]]] = []
    casillas: list[int] = []
    alfas_reales: list[float] = []
    for alfa in ALFAS:
        m = primo_cercano(N_FIJO / alfa)
        lista, tabla = construir(envios, m)
        verificar(lista, tabla, envios)
        casos.append((tabla, inexistentes))
        casillas.append(m)
        alfas_reales.append(tabla.factor_carga())

    tiempos = tiempos_medios(casos)

    print(f"\nExperimento B: n = {N_FIJO}, guias inexistentes")
    print(f"{'m':>7} {'alfa':>6} {'tabla (us)':>12}")
    for m, alfa, t_tabla in zip(casillas, alfas_reales, tiempos):
        print(f"{m:>7} {alfa:>6.2f} {t_tabla * 1e6:>12.3f}")
    return alfas_reales, tiempos


def graficar_a(tiempos_lista: list[float], tiempos_tabla: list[float]) -> None:
    """Guarda la grafica de tiempo medio frente a n.

    Dibuja dos paneles con las mismas curvas: escala lineal (para ver
    la forma) y escala logaritmica (para que la tabla no se pegue al eje).

    Args:
        tiempos_lista: tiempos medios de la lista, en segundos.
        tiempos_tabla: tiempos medios de la tabla, en segundos.
    """
    lista_us = [t * 1e6 for t in tiempos_lista]
    tabla_us = [t * 1e6 for t in tiempos_tabla]
    figura, (lineal, logaritmica) = plt.subplots(1, 2, figsize=(13, 5.5))
    for eje in (lineal, logaritmica):
        eje.plot(TAMANOS, lista_us, marker="o", color="crimson",
                 label="Lista enlazada, Θ(n)")
        eje.plot(TAMANOS, tabla_us, marker="s", color="dodgerblue",
                 label="Tabla hash (α ~ 2), Θ(1 + α)")
        eje.set_xlabel("Número de guías n")
        eje.set_ylabel("Tiempo medio por búsqueda (µs)")
        eje.grid(True, linestyle="--", alpha=0.6)
        eje.legend()
    lineal.set_title("Escala lineal")
    logaritmica.set_title("Escala logarítmica en ambos ejes")
    logaritmica.set_xscale("log")
    logaritmica.set_yscale("log")
    figura.suptitle("Búsqueda de guías inexistentes: lista enlazada vs. "
                    "tabla hash", fontweight="bold")
    figura.tight_layout()
    figura.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close(figura)


def graficar_b(alfas: list[float], tiempos: list[float]) -> None:
    """Guarda la grafica de tiempo medio frente al factor de carga.

    Args:
        alfas: factores de carga medidos.
        tiempos: tiempos medios de la tabla, en segundos.
    """
    figura, eje = plt.subplots(figsize=(8, 5.5))
    eje.plot(alfas, [t * 1e6 for t in tiempos], marker="s",
             color="dodgerblue", label=f"Tabla hash, n = {N_FIJO}")
    eje.set_title("Tiempo de búsqueda de guías inexistentes vs. factor "
                  "de carga", fontweight="bold")
    eje.set_xlabel("Factor de carga α = n / m (guías por casilla)")
    eje.set_ylabel("Tiempo medio por búsqueda (µs)")
    eje.grid(True, linestyle="--", alpha=0.6)
    eje.legend()
    figura.tight_layout()
    figura.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close(figura)


def main() -> None:
    """Ejecuta los dos experimentos y guarda sus graficas."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    tiempos_lista, tiempos_tabla = experimento_a()
    graficar_a(tiempos_lista, tiempos_tabla)
    alfas, tiempos = experimento_b()
    graficar_b(alfas, tiempos)
    print(f"\nGraficas guardadas en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
