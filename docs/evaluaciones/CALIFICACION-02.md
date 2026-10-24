# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Juliana Gómez Legarda · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `b836076`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 14 / 25 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **73 / 100** |
| **Nota (0–5)** | **3.65** |

## 1. Corrección conceptual (15 / 20)
**Lo que hizo bien:**
- Explica bien por qué dividir no ayuda para hallar el máximo de un arreglo: combinar cuesta poco y el resultado sigue siendo `Θ(n)`.
- Recomienda divide y vencerás y declara que el tiempo para 1.000.000 de registros es una estimación, no una regla de tres lineal.

**Lo que puede mejorar:**
- Su estimación parte de "0.003 segundos con n = 8000", pero en su gráfica publicada la curva de divide y vencerás en n = 8000 está cerca de 0.02 segundos. La estimación debe apoyarse en lo que muestra su propia gráfica.
- En la pregunta 3 dice que la ventaja aparece desde n = 500 o 1000, pero no muestra los valores que lo respaldan; en la gráfica los tamaños pequeños no se distinguen.
- No da un tiempo aproximado para la fuerza bruta con 1.000.000 de registros, solo dice "horas o días".

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica de dónde sale cada término y lo resuelve con el método maestro verificando que `f(n)` empata con `n`.
- Justifica el `Θ(n²)` de la fuerza bruta con la suma `n(n+1)/2`.

**Lo que puede mejorar:**
- Falta decir explícitamente por qué el caso cruzado cuesta `Θ(n)` en función del tamaño del rango (cada barrido recorre una mitad).

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias; no modifican la lista y `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- `pruebas.py` cubre todos los casos pedidos con 25 listas aleatorias.

**Lo que puede mejorar:**
- `medir_rendimiento` no tiene docstring ni tipo de retorno de estilo Google completo (sin sección de qué hace ni argumentos).

## 4. Calidad del análisis de las gráficas (14 / 25)
**Lo que hizo bien:**
- La gráfica existe, tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 7 tamaños (de 10 a 8000).
- Repitió cada medición 3 veces y lo explica.

**Lo que puede mejorar:**
- La gráfica no está incrustada en el `README.md`, así que el informe no la muestra; esto limita este criterio.
- En la pregunta 2 dice "cercano a 4" y "alrededor de 2.1 o 2.2" sin dar los tiempos usados. En su gráfica la fuerza bruta pasa de cerca de 0.7 s (n = 4000) a cerca de 2.8 s (n = 8000), es decir, unas 4 veces; debe escribir esos valores y el cálculo.

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, tiene su nombre y hay más de tres commits con mensajes descriptivos.
- La carpeta `laboratorios/lab2-divide-y-vencer/` es una ubicación válida y tiene todos los archivos del entregable.

**Lo que puede mejorar:**
- Los enlaces a `subarreglo.py`, `pruebas.py` y `medicion.py` están escritos entre corchetes pero sin dirección, así que no llevan a ningún archivo.
- Falta la imagen de la gráfica en la sección "Gráfica de Desempeño".
- Las instrucciones de reproducción tienen un bloque de código sin cerrar y las rutas (`lab2-divide-y-vencer/...`) no coinciden con la ubicación real dentro de `laboratorios/`.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas soluciones dan siempre la misma suma y el script de medición corre y genera la gráfica.

## Para el próximo laboratorio
- Incruste las gráficas en el `README.md` con ruta relativa y revise en la vista de GitHub que se vean.
- Escriba los enlaces completos a cada archivo de código.
- Apoye cada cifra del análisis y de las estimaciones en valores leídos de su propia gráfica o tabla, y muéstrelos.
- Cierre los bloques de código del README y verifique que los comandos funcionen desde la ubicación real.
- Agregue docstring (con Args y Returns) y type hints en todas las funciones, incluidas las de medición.
