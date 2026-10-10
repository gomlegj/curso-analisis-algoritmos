# Laboratorio 2 — Dividir y Vencer (Subarreglo Máximo)

**Estudiante:** Juliana Gómez Legarda  
**Curso:** Análisis de Algoritmos  

## Instrucciones de Reproducción

Buen día, por favor siga las instrucciones a continuación:
1. Active el entorno virtual ubicado en la raíz del repositorio.
2. Asegúrese de tener instaladas las dependencias (incluyendo `matplotlib`). Puede verificarlo o instalarlas con:
   ```bash
   pip install -r requirements.txt


Para ejecutar las pruebas unitarias automatizadas:
   python lab2-divide-y-vencer/pruebas.py

   Para ejecutar el experimento de medición y generar la gráfica de desempeño:
   python lab2-divide-y-vencer/medicion.py

## Parte 1 — Implementación y Verificación

Los códigos fuente de la práctica están organizados en el repositorio:

* [subarreglo.py]
* [pruebas.py]

### ¿Cómo verificamos que esto funciona?

Montamos un set de pruebas bien completo en `pruebas.py` utilizando `assert` para asegurar que no se nos pasara ningún caso extremo. Validamos lo siguiente:

* **El caso de la cooperativa:** La famosa serie de ocho días `[-3, 5, -2, 8, -6, 3, 9, -4]` donde el resultado óptimo da 17.
* **Caso base unitario:** Una listica de un solo elemento para que la recursión no se rompa al llegar al fondo.
* **Extremos de signos:** Una lista con puras pérdidas (todos negativos) y otra con puras ganancias (todos positivos).
* **El cruce obligatorio:** Un caso diseñado a mano donde el mejor subarreglo atraviesa el punto medio exacto (`medio`), obligando a `suma_cruzada` a jalar bien los punteros.
* **Prueba de estrés aleatoria:** Generamos 25 listas aleatorias con tamaños variados (usando semilla fija) y comparamos exhaustivamente que el resultado de fuerza bruta y el de divide y vencerás dieran exactamente la misma suma máxima.

---

## Parte 2 — Medición y Gráfica

El script de experimentación se puede consultar en [medicion.py]

### Metodología de las pruebas de tiempo

* **Tamaños evaluados (n):** 10, 50, 100, 500, 1000, 4000 y 8000.
* **Mitigación de ruido:** Para evitar que las fluctuaciones del sistema operativo arruinaran los datos, ejecutamos cada medición 3 veces seguidas con `time.perf_counter()` y sacamos el promedio aritmético.
* **Aislamiento:** La generación de las listas aleatorias se hace por fuera del cronómetro; solo medimos el tiempo exacto que gasta el algoritmo ejecutando la función.
* **Control de sanidad:** En cada iteración del experimento, el script valida automáticamente que ambos algoritmos devuelvan la misma suma.

### Gráfica de Desempeño

---

## Parte 3 — Análisis

### 1. Recurrencia

La función `subarreglo_maximo` divide el problema en dos mitades simétricas de tamaño `n / 2`, haciendo dos llamadas recursivas. Por su parte, la función `suma_cruzada` hace dos barridos lineales independientes desde el centro hacia los extremos, lo que toma un tiempo proporcional a Theta(n). Con esto, la ecuación de recurrencia queda planteada como:

`T(n) = 2T(n/2) + Theta(n)`

Si aplicamos el Método Maestro para recurrencias de la forma `T(n) = aT(n/b) + f(n)`:

* Tenemos que `a = 2`, `b = 2` y `f(n) = Theta(n)` (donde `k = 1`).
* Calculamos `n^(log_b a) = n^(log_2 2) = n^1 = n`.
* Como `f(n) = Theta(n)` empata exactamente con `n^(log_b a)` (`f(n) = Theta(n^(log_b a) * log^0 n`), caemos en el Caso 2 del método maestro.
* Por lo tanto, la complejidad temporal analítica es `T(n) = Theta(n log n)`.

En cuanto a la fuerza bruta, evalúa todos los pares posibles de índices `(i, j)` mediante dos ciclos anidados. Al ir acumulando la suma de forma incremental en el ciclo interno, el número total de operaciones viene dado por la sumatoria de los tramos, lo cual resulta en `n * (n + 1) / 2`, es decir, una complejidad de `Theta(n^2)`.

### 2. Lo medido contra lo esperado

Al mirar la gráfica, se nota clarísimo el comportamiento de las curvas: la fuerza bruta se dispara de forma vertical (crecimiento cuadrático), mientras que divide y vencerás se mantiene prácticamente plana pegada al eje horizontal.

Si tomamos dos tamaños consecutivos donde `n` se duplica, por ejemplo de `n = 4000` a `n = 8000`:

* **Fuerza Bruta:** El tiempo se multiplica por un factor cercano a 4 (`2^2`), lo cual encaja perfecto con lo que predice la teoría para `Theta(n^2)`.
* **Divide y Vencerás:** El factor de crecimiento al duplicar la entrada está un poco por encima de 2 (alrededor de 2.1 o 2.2), lo cual es totalmente consistente con el comportamiento cuasi-lineal de `Theta(n log n)` debido al término logarítmico.

### 3. Tamaños pequeños

En nuestras mediciones, la ventaja de divide y vencerás empieza a notarse de verdad a partir de `n = 500` o `n = 1000`. Para entradas muy chiquitas (`n = 10` o `n = 50`), los tiempos son tan ínfimos (del orden de microsegundos) que la sobrecarga (*overhead*) de las llamadas recursivas y la gestión de la pila en Python hace que la fuerza bruta compita codo a codo o parezca ligeramente más rápida en ejecuciones aisladas. La superioridad asintótica de divide y vencerás solo se vuelve evidente cuando `n` crece lo suficiente como para que el término cuadrático de la fuerza bruta aplaste cualquier sobrecarga de la recursión.

### 4. ¿Cuándo conviene dividir?

Dividir un problema a la mitad no siempre da una ventaja mágica así como lo explocaba el profesor en la clase, por lo que pensé en un problema clásico y distinto: hallar el máximo de un arreglo de `n` números.

* Si lo resuelvo aplicando divide y vencerás (partiendo el arreglo en dos, buscando el máximo de la izquierda y el de la derecha, y combinándolos con un `max`), la recurrencia sería `T(n) = 2T(n/2) + Theta(1)`, cuya solución por el método maestro da `Theta(n)`.
* Sin embargo, si simplemente recorro el arreglo una sola vez de forma lineal, también obtenemos tiempo `Theta(n)`.
* Conclusión: aquí dividir no sirve de nada. El costo de combinar es insignificante (`Theta(1)`), por lo que no compensa la sobrecarga de la recursión. El paradigma de divide y vencerás solo funciona cuando el paso de combinación o los subproblemas hacen un trabajo pesado (como el caso cruzado en el subarreglo máximo o las mezclas en MergeSort) que es mejorado por la reducción logarítmica de la altura del árbol de recursión.

### 5. Concepto para la gerente

Si la cooperativa necesita analizar series de datos de sensores con cientos de miles o incluso millones de registros, la recomendación sería: **hay que usar Divide y Vencerás**.

**Estimación del tiempo para 1.000.000 de registros:**

* *Aclaración:* Es una estimación basada en la tendencia empírica y la complejidad teórica, no una simple regla de tres lineal.
* Con `n = 8000`, divide y vencerás se demora más o menos 0.003 segundos. Si escalamos a `n = 1.000.000` (un factor de escala de aprox. 125), el aumento de tiempo se calcula ajustando por el factor logarítmico: `(1.000.000 / 8.000) * (log_2(1.000.000) / log_2(8.000))` que da aprox. `125 * (19.93 / 12.97) = 192` veces.
* Esto nos da un tiempo estimado de apenas unos **0.6 segundos** para procesar un millón de registros con divide y vencerás.
* En el otro extremo, intentar correr 1.000.000 de registros con fuerza bruta (`Theta(n^2)`) implicaría un factor de crecimiento de `125^2 = 15.625` veces, lo que se traduciría en horas o días de procesamiento continuo, volviendo el sistema totalmente inviable en la práctica.

En conclusión, recomendaría divide y vencerás porque permite procesar grandes cantidades de datos de manera mucho más eficiente. Aunque ambos algoritmos encuentran la misma suma máxima, la diferencia en su complejidad hace que fuerza bruta sea una opción poco conveniente para trabajar con millones de registros.
