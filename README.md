# A01796384_A4.2
4.2 Ejercicio de programación 1

- Implementación en **Python**
- Estilo **PEP 8**
- Análisis de calidad con **pylint** (cero errores para máxima calificación)
- Ejecución de **casos de prueba** y **evidencia** en archivos de resultados

## Estructura del repositorio
```text
A01796384_A4.2/
├── p1_stats/
│ ├── compute_statistics.py
│ └── tests/
│ ├── TC1.txt ... TC7.txt
│ └── statistics_results.txt
├── p2_transform/
│ ├── convert_numbers.py
│ └── tests/
│ ├── TC1.txt ... TC4.txt
│ └── convertion_results.txt
├── p3_wordcount/
│ ├── word_count.py
│ └── tests/
│ ├── TC1.txt ... (según archivos de apoyo)
│ └── word_count_results.txt
└── README.md
```

> Los **archivos de resultados** se generan en modo *append* para dejar evidencia de múltiples ejecuciones en un solo archivo.

---

## Requisitos generales (según instrucciones)

1. Implementar los 3 programas en Python.
2. Seguir el estándar **PEP 8**.
3. Verificar ejecución con **casos de prueba** (archivos proporcionados) y documentar resultados.
4. Instalar y ejecutar **pylint**.
5. Corregir detalles reportados por pylint y confirmar que el programa siga funcionando.

---

## Instalación (entorno local o Codespaces)

Verifica que `python` esté disponible.

Instala pylint:
```bash
pip install pylint
```
---

## Programa 1 — Compute statistics (p1_stats)
Qué hace

Lee un archivo con números (uno por línea) y calcula:

1. n, mean, median, mode, std dev (muestral), variance (muestral), min, max
2. Maneja líneas inválidas: muestra Warning y continúa
3. Muestra resultados en consola y los guarda en:
```bash
p1_stats/tests/statistics_results.txt
```
4. Incluye tiempo transcurrido

## Ejecutar un caso

Desde la raíz del repo:
```bash
python p1_stats/compute_statistics.py p1_stats/tests/TC1.txt
```
O entrando a la carpeta:
```bash
cd p1_stats
python compute_statistics.py tests/TC1.txt
```
## Ejecutar todos los casos (TC1-TC7)
```bash
python p1_stats/compute_statistics.py p1_stats/tests/TC1.txt
python p1_stats/compute_statistics.py p1_stats/tests/TC2.txt
python p1_stats/compute_statistics.py p1_stats/tests/TC3.txt
python p1_stats/compute_statistics.py p1_stats/tests/TC4.txt
python p1_stats/compute_statistics.py p1_stats/tests/TC5.txt
python p1_stats/compute_statistics.py p1_stats/tests/TC6.txt
python p1_stats/compute_statistics.py p1_stats/tests/TC7.txt
```

Evidencia: revisar/entregar p1_stats/tests/statistics_results.txt.

## Pylint PEP8
```bash
pylint p1_stats/compute_statistics.py
```
