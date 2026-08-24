"""Clasificador de años bisiestos. """


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
  
    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese una lista de años separados por comas: ")
        try:
            # Separa por comas, elimina espacios en blanco y convierte a entero
            anios = [int(a.strip()) for a in entrada.split(",")]
            return anios
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas. Inténtelo de nuevo.")


def main() -> None:
    """Punto de entrada del script."""
    anios_ingresados = leer_anios()
    
    # Filtra los años bisiestos usando comprensión de listas
    anios_bisiestos = [anio for anio in anios_ingresados if es_bisiesto(anio)]
    
    # Muestra el resumen solicitado
    print("\n--- Resumen de Clasificación ---")
    print(f"Años ingresados: {anios_ingresados}")
    print(f"Años bisiestos encontrados: {anios_bisiestos}")
    print(f"Cantidad total de años bisiestos: {len(anios_bisiestos)}")


if __name__ == "__main__":
    main()


