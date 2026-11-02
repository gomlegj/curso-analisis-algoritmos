# Retroalimentación — Lab 03: Estructuras de datos

**Estudiante:** Juliana Gómez Legarda · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-02 23:59 · **Versión revisada:** commit `f374bea`

Muy buen trabajo: el código funciona, las gráficas son claras y el informe se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **97 / 100** |
| **Nota (0–5)** | **4.85** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque sobren casillas, con el ejemplo de las guías 10, 24 y 17 con `m = 7` y el cálculo de la probabilidad de que no choquen.
- Compara el encadenamiento con el direccionamiento abierto, con ventajas y costos de cada uno, y los ilustra con el mismo ejemplo.
- Justifica por qué la tabla no sirve para rangos y estima bien la altura del árbol degenerado (unos 400.000 niveles) frente a la del equilibrado (unos 19), con la comparación entre ambos.
- Recomienda una combinación (tabla hash para el call center y árbol equilibrado para rangos) y declara la estimación a 5.000.000 como estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación de la tabla a 5.000.000 de envíos pasa de unos 0,37 µs a "cerca de 1 µs" sin explicar cuánto aporta cada efecto; ese salto queda sin respaldo en sus datos.
  → *Cómo corregirlo:* use la parte de su primera gráfica donde la tabla sube con n y diga qué tendencia observa y hasta dónde la extendería, de modo que el número final salga de una cuenta que se pueda seguir.
- En la estimación de la lista, el costo por guía va creciendo con n y usted lo reconoce, pero el rango final (0,35 a 0,5 s) no se explica con cifras.
  → *Cómo corregirlo:* calcule el costo por guía en los valores de n que midió, mire cómo cambia y úselo para justificar el rango que propone.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista (compara con los n nodos cuando la guía no existe).
- Justifica el `Θ(1 + α)` de la tabla: un paso fijo para calcular la casilla más la cadena promedio de α guías.
- Nombra el supuesto de hash uniforme simple y explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista con costo `Θ(n)`.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` inserta al inicio y busca con un `while`, sin recursión.
- `TablaHash` reutiliza la lista en cada casilla, usa `guia % m` y no emplea `dict`, `set` ni `hash()`.
- `pruebas.py` cubre búsquedas exitosas e infructuosas, la colisión forzada con `m = 7` (casilla 3 con longitud 3), `factor_carga() == 3 / 7` y 25 colecciones aleatorias que comparan lista y tabla con guías existentes e inexistentes.
- Todas las funciones tienen *type hints*, *docstrings* con `Args` y `Returns`, y dos líneas en blanco entre ellas.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados con unidades y leyenda. La primera cubre seis valores de `n` con las dos curvas en los mismos ejes (en escala lineal y logarítmica) y la segunda cubre seis valores de `α`.
- En la pregunta 2 calcula factores de crecimiento (por ejemplo 500 a 1.000 y 5.000 a 20.000) y los contrasta con `Θ(n)` y `Θ(1)`. Los valores que cita coinciden con lo que se lee en las gráficas publicadas.
- Ajusta una recta al experimento B, predice el valor para α = 4 y lo compara con lo medido, lo que respalda `Θ(1 + α)`.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab3-estructuras-datos/` está en una ubicación válida y trae todos los archivos pedidos: `README.md`, `estructuras.py`, `pruebas.py`, `medicion.py` y las dos gráficas en `graficas/`.
- El informe sigue el orden pedido, trae su nombre e instrucciones de reproducción, enlaza el código al inicio de cada parte práctica y las dos imágenes se ven con ruta relativa.
- La nota sobre cómo midió (repeticiones, `m` usado en cada `n`) es clara.

**Lo que puede mejorar (y cómo corregirlo):**
- Faltan commits: el laboratorio tiene solo dos commits, y se piden al menos tres descriptivos. Además, "graficas e informe lab03" junta dos cosas distintas y dice poco.
  → *Cómo corregirlo:* haga un commit por avance (estructuras, pruebas, medición, gráficas, informe) con mensajes que digan qué cambió, por ejemplo `git commit -m "Agrega pruebas de colision forzada con m = 7"`.

## ¿El código funciona?
Sí. Las pruebas pasan completas y la medición corre sin errores y genera las dos gráficas. Lista y tabla devuelven lo mismo en todas las comprobaciones.
