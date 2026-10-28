"""Pruebas con assert de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ("en bodega", "en reparto", "entregado", "devuelto")

# 1. Estructuras vacías: cualquier búsqueda debe dar None.
assert ListaEnlazada().buscar(1000000010) is None
assert TablaHash(7).buscar(1000000010) is None

# 2. Serie de ejemplo de Rutas del Caribe: una guía que sí está y otra  que no, en la lista y en la tabla.
serie = [
    (1000000010, "en bodega"),
    (1000000024, "en reparto"),
    (1000000017, "en bodega"),
    (1000000005, "entregado"),
]
lista = ListaEnlazada()
tabla = TablaHash(7)
for guia, estado in serie:
    lista.insertar(guia, estado)
    tabla.insertar(guia, estado)

assert lista.tamano == 4 and tabla.tamano == 4
for guia, estado in serie:
    assert lista.buscar(guia) == estado
    assert tabla.buscar(guia) == estado
# Un numero mal digitado: esta guía no existe en ninguna de las dos.
assert lista.buscar(1000000011) is None
assert tabla.buscar(1000000011) is None

# 3. Colisión forzada: con m = 7, las guías 10, 24 y 17 caen en la casilla 3.
tabla = TablaHash(7)
for guia in (10, 24, 17):
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, "en bodega")

assert tabla.buscar(10) == "en bodega"
assert tabla.buscar(24) == "en bodega"
assert tabla.buscar(17) == "en bodega"
# Las tres comparten casilla, así que esa lista debe tener longitud 3 y
# las demás casillas deben seguir vacías.
assert tabla.casillas[3].tamano == 3
assert all(tabla.casillas[i].tamano == 0 for i in range(7) if i != 3)
# 31 también cae en la casilla 3 pero no la inserté: recorre la cadena
# completa y debe devolver None.
assert tabla.buscar(31) is None
assert tabla.buscar(99) is None

# 4. Factor de carga tras las tres inserciones.
assert tabla.factor_carga() == 3 / 7

# 5. Veinticinco colecciones aleatorias: lista y tabla deben responder lo
# mismo para guías existentes e inexistentes.
azar = random.Random(2026)
for _ in range(25):
    n = azar.randint(1, 300)
    m = azar.randint(1, 50)
    guias = azar.sample(range(10**9, 10**10), n)
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    for guia in guias:
        assert lista.buscar(guia) == tabla.buscar(guia) is not None

    # Las guías de nueve dígitos nunca pueden estar en una colección de guías de diez dígitos, así que son inexistentes seguras.
    for guia in azar.sample(range(10**8, 10**9), 30):
        assert lista.buscar(guia) is None
        assert tabla.buscar(guia) is None

    assert tabla.factor_carga() == n / m

print("Todas las pruebas pasaron.")
