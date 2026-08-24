# def CalcularPromedio(Lista):
#     s=0
#     for x in Lista:
#      s=s+x
#     return s/len(Lista)
 
# l=[1,2,3,4,5]
# print(CalcularPromedio(l))


from typing import List


def calcular_promedio(lista_valores: List[float]) -> float:
    """Calcula el promedio aritmético de una lista de números.

    Args:
        lista_valores (List[float]): Lista de números a promediar.

    Returns:
        float: El valor promedio de los elementos de la lista.
    """
    suma_total = 0.0
    for numero in lista_valores:
        suma_total += numero
    return suma_total / len(lista_valores)


def main() -> None:
    """Función principal que ejecuta el ejemplo de cálculo de promedio."""
    numeros = [1, 2, 3, 4, 5]
    resultado = calcular_promedio(numeros)
    print(resultado)


if __name__ == "__main__":
    main()