# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Juliana Gómez Legarda · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-11-02 23:59 · **Versión revisada:** commit `f374bea`

Excelente trabajo: un informe muy completo, con datos propios y buen razonamiento.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 24 / 25 |
| Calidad de la explicación teórica | 24 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 19 / 20 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (24 / 25)
**Lo que hizo bien:**
- Distingue con claridad lo correcto de lo viable y nombra la restricción que se incumple: ordenar 1.200.000 registros dentro de la ventana de cuatro horas.
- Explica por qué duplicar la velocidad del servidor no arregla el fondo del problema, apoyándose en que el trabajo crece con el cuadrado de n.
- El segundo ejemplo (matrícula universitaria) trae datos aproximados y la restricción que se rompe (el tiempo de respuesta de la página).
- En lo ambiental relaciona horas de cómputo con energía acumulada a lo largo del año. En lo ético identifica a varias personas afectadas y dice quién asume el costo de cada caso.
- Discute bien la tensión del orden: verificar la salida, definir los empates y avisar cuando el proceso falla.

**Lo que puede mejorar (y cómo corregirlo):**
- En el segundo ejemplo, la cifra de comparaciones por segundo se da sin explicar de dónde sale, y la solución que propone (agrupar por estudiante) se menciona solo de pasada.
  → *Cómo corregirlo:* diga en una frase en qué se basa esa velocidad (una suposición suya o algo que midió) y explique brevemente por qué agrupar primero evita comparar todo contra todo.

## 2. Calidad de la explicación teórica (24 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y promedio indicando sobre qué conjunto de entradas se toma cada uno, con tamaño fijo, y justifica que usaría el peor caso por ser estricta la ventana.
- La predicción quedó escrita antes del experimento y la contrasta después, explicando con números por qué el escenario B no es el mejor caso en sentido estricto.
- La recurrencia de merge sort está bien planteada, con cada término explicado, y la resolución por árbol de recursión incluye el dibujo, el costo por nivel, el número de niveles y el costo total.
- El análisis línea a línea de insertion sort y la tabla de complejidades por caso están completos y son coherentes con lo medido.

**Lo que puede mejorar (y cómo corregirlo):**
- En el árbol de recursión se pasa de la suma por niveles a Θ(n log n) sin decir por qué el término cn pesa menos que cn·log n.
  → *Cómo corregirlo:* agregue una línea que compare los dos términos de la suma cuando n crece y diga cuál domina.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor, criterio declarado y usado en todo el laboratorio), no alteran la lista recibida y cuentan solo comparaciones entre elementos. Con una lista ya ordenada de 100 elementos, insertion sort cuenta 99.
- `merge_sort` tiene su propia mezcla recursiva y no se usa `sorted()` ni `list.sort()`.
- Los tres generadores dan listas del tamaño pedido, sin repetidos, y los aleatorios aceptan semilla y se repiten igual.
- Hay docstrings con `Args` y `Returns`, anotaciones de tipo y dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- Algunas funciones auxiliares de los scripts de medición tienen docstring más corto que el estilo pedido: `main` y `medir_tamanos_pequenos` no traen `Returns`.
  → *Cómo corregirlo:* agregue una sección `Returns:` (por ejemplo "Nada, solo imprime y guarda gráficas") o `None` en esas funciones, para que todas sigan el mismo formato.

## 4. Calidad del análisis de las gráficas (19 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica con evidencia el peor caso (C), el mejor (B) y el que se acerca al promedio (A). Las cifras que cita coinciden con lo que se ve en las gráficas publicadas.
- Concluye que merge sort conviene para Tamiza describiendo lo que hace cada curva, lo contrasta con las complejidades de 4.1 y explica el comportamiento con listas pequeñas.
- El concepto técnico recomienda un solo algoritmo, responde a la propuesta del servidor con un dato medido (n = 6.400), extrapola a 1.200.000 registros declarándolo como estimación y discute memoria, estabilidad y el riesgo del escenario B.

**Lo que puede mejorar (y cómo corregirlo):**
- En 4.3 se extrapola una sola medición por escenario y no se aclara cuánto puede cambiar el resultado si la medición varía.
  → *Cómo corregirlo:* mencione en una frase que la estimación hereda el ruido de los tiempos medidos y dé un rango, como ya hizo con el escenario A.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en `laboratorios/lab1-fundamentos-complejidad-recurrencias/`, una ubicación válida, con todos los archivos del entregable.
- El README tiene su nombre, instrucciones para reproducir, las partes en orden, las gráficas incrustadas con ruta relativa que sí resuelve, y enlaces al código de cada parte práctica, a `algoritmos.py` y a `datos.py`.

**Lo que puede mejorar (y cómo corregirlo):**
- Solo hay 3 commits que tocan este laboratorio y se pedían al menos cinco que documenten el avance. Además los mensajes son muy generales ("Laboratorio 01 añadido", "fix: Ajustes readme").
  → *Cómo corregirlo:* haga un commit por cada pieza terminada (algoritmos, generadores, Parte 3, Parte 4, cada sección del informe) con un mensaje que diga qué se hizo.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien con listas pequeñas y aleatorias, y los scripts de las Partes 3 y 4 corren sin errores y generan las gráficas. Los números de comparaciones coinciden con los del informe.
