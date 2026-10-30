"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1.

Todo el laboratorio ordena de MAYOR a MENOR índice de riesgo, que es como
Tamiza necesita la lista de llamadas: el paciente con más riesgo va de
primero. Los generadores de datos.py siguen el mismo criterio.
"""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    # Trabajo sobre una copia porque el mismo lote se vuelve a usar en
    # las otras repeticiones de la medición.
    arreglo = list(datos)
    comparaciones = 0

    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1

        # La condición j >= 0 quedó sola en el while a propósito: así el
        # contador solo suma cuando de verdad se comparan dos índices de
        # riesgo (arreglo[j] < clave) y no cuando se revisa el límite.
        while j >= 0:
            comparaciones += 1
            if arreglo[j] < clave:
                # Si el de la izquierda tiene menos riesgo, se corre una
                # posición a la derecha y le deja el hueco a la clave.
                arreglo[j + 1] = arreglo[j]
                j -= 1
            else:
                # Ya está en su sitio, no tiene sentido seguir comparando.
                break

        arreglo[j + 1] = clave

    return arreglo, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    # Con list(datos) la lista original queda intacta; de ahí en adelante
    # la recursión solo toca la copia y las sublistas que salen de ella.
    return _merge_sort_recursivo(list(datos))


def _merge_sort_recursivo(arreglo: list[int]) -> tuple[list[int], int]:
    """Divide la lista, ordena cada mitad y las mezcla.

    Args:
        arreglo: lista (ya copiada) que se va a ordenar.

    Returns:
        Una tupla con la lista ordenada de mayor a menor y las
        comparaciones hechas en esta llamada y en sus subllamadas.
    """
    # Una lista vacía o de un elemento ya está ordenada.
    if len(arreglo) <= 1:
        return arreglo, 0

    # Dividir en dos mitades de tamaño n/2.
    mitad = len(arreglo) // 2
    # Cada mitad se ordena con la misma función.
    izquierda, comp_izq = _merge_sort_recursivo(arreglo[:mitad])
    derecha, comp_der = _merge_sort_recursivo(arreglo[mitad:])
    # Por último la mezcla, que recorre las dos mitades una sola vez.
    mezclada, comp_mezcla = _mezclar(izquierda, derecha)

    return mezclada, comp_izq + comp_der + comp_mezcla


def _mezclar(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos listas ordenadas de mayor a menor en una sola.

    Args:
        izquierda: lista ordenada de mayor a menor.
        derecha: lista ordenada de mayor a menor.

    Returns:
        Una tupla con la lista combinada y el número de comparaciones
        entre elementos que hizo la mezcla.
    """
    resultado: list[int] = []
    comparaciones = 0
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        # Con >= en un empate gana el de la izquierda, que venía antes;
        # eso es lo que hace que el ordenamiento sea estable.
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Cuando una lista se acaba, lo que queda en la otra ya está en orden.
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones
