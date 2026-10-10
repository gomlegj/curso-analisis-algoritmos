"""Script de pruebas automatizadas con assert para el laboratorio."""

import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_pruebas() -> None:
    # 1. Serie de ocho días de la situación problema (suma esperada: 17)
    serie_problema = [-3, 5, -2, 8, -6, 3, 9, -4]
    res_fb = subarreglo_fuerza_bruta(serie_problema)
    res_dv = subarreglo_maximo(serie_problema, 0, len(serie_problema) - 1)
    assert res_fb[2] == 17, f"Fuerza bruta falló en caso base: {res_fb[2]}"
    assert res_dv[2] == 17, f"Divide y vencerás falló en caso base: {res_dv[2]}"

    # 2. Serie de un solo elemento
    serie_unitaria = [42]
    assert subarreglo_fuerza_bruta(serie_unitaria)[2] == 42
    assert subarreglo_maximo(serie_unitaria, 0, 0)[2] == 42

    # 3. Serie con todos los valores negativos
    serie_negativa = [-5, -2, -9, -1]
    # El mayor subarreglo con elementos negativos toma el menor negativo (-1)
    assert subarreglo_fuerza_bruta(serie_negativa)[2] == -1
    assert subarreglo_maximo(serie_negativa, 0, len(serie_negativa) - 1)[2] == -1

    # 4. Serie con todos los valores positivos
    serie_positiva = [2, 4, 6, 8]
    suma_total = sum(serie_positiva)
    assert subarreglo_fuerza_bruta(serie_positiva)[2] == suma_total
    assert (
        subarreglo_maximo(serie_positiva, 0, len(serie_positiva) - 1)[2]
        == suma_total
    )

    # 5. Caso explícito donde el mejor tramo cruza el punto medio
    # [10, -3, -3, 10] -> El medio cae en el segundo -3. El tramo completo suma 14.
    serie_cruzada = [10, -3, -3, 10]
    assert subarreglo_fuerza_bruta(serie_cruzada)[2] == 14
    assert (
        subarreglo_maximo(serie_cruzada, 0, len(serie_cruzada) - 1)[2] == 14
    )

    # 6. Al menos veinte listas aleatorias comparando ambas soluciones
    random.seed(42)
    for i in range(25):
        tam = random.randint(5, 50)
        serie_aleatoria = [random.randint(-50, 50) for _ in range(tam)]
        s_fb = subarreglo_fuerza_bruta(serie_aleatoria)[2]
        s_dv = subarreglo_maximo(
            serie_aleatoria, 0, len(serie_aleatoria) - 1
        )[2]
        assert s_fb == s_dv, (
            fiteración {i} con tamaño {tam}: FB dio {s_fb} y DV dio {s_dv}"
        )

    print("¡Todas las pruebas pasaron exitosamente!")


if __name__ == "__main__":
    ejecutar_pruebas()