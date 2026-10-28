"""Lista enlazada y tabla hash para consultar guias de envio."""


class Nodo:
    """Nodo de una lista enlazada que guarda una guia y su estado."""

    def __init__(self, guia: int, estado: str) -> None:
        """Crea un nodo sin siguiente.

        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        self.guia = guia
        self.estado = estado
        self.siguiente: Nodo | None = None


class ListaEnlazada:
    """Lista simplemente enlazada de guias, con insercion al inicio."""

    def __init__(self) -> None:
        """Crea una lista vacia."""
        self.cabeza: Nodo | None = None
        self.tamano = 0

    def insertar(self, guia: int, estado: str) -> None:
        """Agrega una guia al inicio de la lista.

        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        # El nodo nuevo apunta a la cabeza actual y pasa a ser la cabeza.
        # No hay que recorrer nada, por eso cuesta Θ(1).
        nuevo = Nodo(guia, estado)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1

    def buscar(self, guia: int) -> str | None:
        """Busca una guia recorriendo la lista.

        Args:
            guia: numero de guia a buscar.

        Returns:
            El estado del envio, o None si la guia no existe.
        """
        # Lo hice con while y no con recursión: con miles de nodos, una
        # versión recursiva chocaría con el límite de recursión de Python.
        actual = self.cabeza
        while actual is not None:
            if actual.guia == guia:
                return actual.estado
            actual = actual.siguiente
        # Llegar aquí significa que revisé los n nodos y no estaba.
        # Es justo el caso que más le duele al call center.
        return None


class TablaHash:
    """Tabla hash con encadenamiento y funcion hash por division."""

    def __init__(self, m: int) -> None:
        """Crea una tabla con m casillas vacias.

        Args:
            m: numero de casillas de la tabla.
        """
        self.m = m
        self.casillas: list[ListaEnlazada] = [
            ListaEnlazada() for _ in range(m)
        ]
        self.tamano = 0

    def hash(self, guia: int) -> int:
        """Calcula la casilla de una guia con el metodo de la division.

        Args:
            guia: numero de guia.

        Returns:
            Un indice entre 0 y m - 1.
        """
        # Con el método de la división, el residuo siempre queda entre
        # 0 y m - 1, que son justo las casillas que existen.
        return guia % self.m

    def insertar(self, guia: int, estado: str) -> None:
        """Inserta una guia en la lista de su casilla.

        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        # Cada casilla ya es una lista enlazada, así que si dos guías
        # colisionan, simplemente quedan juntas en la misma lista.
        self.casillas[self.hash(guia)].insertar(guia, estado)
        self.tamano += 1

    def buscar(self, guia: int) -> str | None:
        """Busca una guia recorriendo solo la lista de su casilla.

        Args:
            guia: numero de guia a buscar.

        Returns:
            El estado del envio, o None si la guia no existe.
        """
        # Aquí está la ganancia: se recorre una sola casilla, que en
        # promedio tiene α guías, y no las n de toda la colección.
        return self.casillas[self.hash(guia)].buscar(guia)

    def factor_carga(self) -> float:
        """Calcula el factor de carga de la tabla.

        Returns:
            El cociente entre guias almacenadas y casillas (n / m).
        """
        # Como tamano se actualiza en cada inserción, no hace falta
        # recorrer las casillas para contar las guías.
        return self.tamano / self.m
