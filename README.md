# Análisis de Algoritmos

Repositorio del curso **Análisis de Algoritmos**. Aquí se centraliza el trabajo práctico del semestre: ejercicios de clase, laboratorios evaluativos y las herramientas compartidas de medición que se usan en ellos.

## Estructura del repositorio

- `laboratorios/`: contiene una subcarpeta por cada uno de los cinco informes de laboratorio evaluativos del semestre. Cada informe documenta su propio análisis, implementación y resultados.
- `ejercicios-clase/`: código de las sesiones prácticas no evaluativas, incluyendo los ejercicios de Python trabajados en la Semana 2. No forma parte de la calificación, pero sirve como registro de práctica.
- `benchmarks/`: scripts compartidos de medición de tiempos de ejecución y graficación de resultados, reutilizados por los distintos laboratorios evaluativos para mantener consistencia en las mediciones.

## Cómo ejecutar un benchmark

Ejemplo de uso típico de un script de `benchmarks/` para medir el tiempo de ejecución de un algoritmo sobre distintos tamaños de entrada:

```bash
python benchmarks/medir_tiempos.py --algoritmo ordenamiento_burbuja --tamanos 100 1000 10000 --salida resultados.csv
```

## Convenciones

- Cada informe de laboratorio va en su propia subcarpeta dentro de `laboratorios/`, nombrada como `laboratorio-0X`.
- Los scripts de `benchmarks/` no se duplican dentro de cada laboratorio: se importan o se referencian desde ahí.
- Los mensajes de commit describen el cambio concreto realizado, evitando mensajes genéricos como "cambios" o "arreglos".


##  Reproducción del Entorno Virtual

Para recrear y activar el entorno virtual y las dependencias del proyecto desde la raíz del repositorio, se debe seguir estos pasos:

1. **Crear el entorno virtual:**
   ```bash
   python3 -m venv venv

   pip install -r requirements.txt

   ---