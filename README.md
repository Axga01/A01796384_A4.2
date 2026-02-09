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
│ ├── TC1.txt ... TC5.txt
│ └── word_count_results.txt
└── README.md
```

> Los **archivos de resultados** se generan en modo *append* para dejar evidencia de múltiples ejecuciones en un solo archivo.

---

## Requisitos generales

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

### Qué hace
Lee un archivo con números (uno por línea) y calcula:

- n
- mean
- median
- mode
- std dev (poblacional)
- variance (poblacional)
- min
- max

### Condiciones
- Maneja líneas inválidas: muestra *Warning* y continúa
- Muestra resultados en consola y los guarda en:

  `p1_stats/tests/statistics_results.txt`

- Incluye tiempo transcurrido

### Ejecutar un caso

**Desde la raíz del repositorio:**
```bash
python p1_stats/compute_statistics.py p1_stats/tests/TC1.txt
```

**O dentro de la carpeta:**
```bash
cd p1_stats
python compute_statistics.py tests/TC1.txt
python compute_statistics.py tests/TC2.txt
python compute_statistics.py tests/TC3.txt
python compute_statistics.py tests/TC4.txt
python compute_statistics.py tests/TC5.txt
python compute_statistics.py tests/TC6.txt
python compute_statistics.py tests/TC7.txt
```

## Evidencia
Revisar o entregar el archivo:

`p1_stats/tests/statistics_results.txt`

### pylint (PEP 8)
```bash
cd /workspaces/A01796384_A4.2
pylint p1_stats/compute_statistics.py
```
<img width="1226" height="812" alt="image" src="https://github.com/user-attachments/assets/253434ea-b8e0-40e2-acab-c1bc1cbb66ac" />
<img width="799" height="135" alt="image" src="https://github.com/user-attachments/assets/d7c6980a-86b0-474e-b4ed-614695fac73f" />

---

## Programa 2 — Converter (p2_transform)

### Qué hace
Lee un archivo con enteros (uno por línea) y convierte cada número a:

- Binario
- Hexadecimal

### Condiciones
- Implementación con algoritmo básico (sin `bin()`, `hex()` o `format()`)
- Maneja líneas inválidas con *Warning* y continúa
- Muestra resultados en consola y guarda en:

  `p2_transform/tests/convertion_results.txt`

- Incluye tiempo transcurrido

### Ejecutar un caso

**Desde la raíz del repositorio:**
```bash
python p2_transform/convert_numbers.py p2_transform/tests/TC1.txt
python p2_transform/convert_numbers.py p2_transform/tests/TC2.txt
python p2_transform/convert_numbers.py p2_transform/tests/TC3.txt
python p2_transform/convert_numbers.py p2_transform/tests/TC4.txt
```

**O dentro de la carpeta:**
```bash
cd p2_transform
python convert_numbers.py tests/TC1.txt
python convert_numbers.py tests/TC2.txt
python convert_numbers.py tests/TC3.txt
python convert_numbers.py tests/TC4.txt
```

## Evidencia
Revisar o entregar el archivo:

`p2_transform/tests/convertion_results.txt`

### pylint (PEP 8)
Importante: para obtener rating, corre pylint sobre el archivo, no sobre el folder como “módulo”.

```bash
cd /workspaces/A01796384_A4.2
pylint p2_transform/convert_numbers.py
```
<img width="1146" height="801" alt="image" src="https://github.com/user-attachments/assets/d224f6d4-0cdb-4df4-94dd-eea8f3c15cc7" />
<img width="844" height="135" alt="image" src="https://github.com/user-attachments/assets/d3e7eee6-817e-47a2-8d72-b0e0df96bf88" />

---

## Programa 3 — Count Words (p3_wordcount)

### Qué hace
Lee un archivo de texto y cuenta:

- Todas las palabras distintas y su frecuencia

### Condiciones
- Algoritmo básico (sin librerías de conteo)
- Maneja líneas vacías o inválidas con *Warning* y continúa
- Imprime resultados y guarda evidencia en:

  `p3_wordcount/tests/word_count_results.txt`

- Incluye tiempo transcurrido

### Ejecutar un caso

**Desde la raíz del repositorio:**
```bash
python p3_wordcount/word_count.py p3_wordcount/tests/TC1.txt
```

**O dentro de la carpeta:**
```bash
cd p3_wordcount
python word_count.py tests/TC1.txt
python word_count.py tests/TC2.txt
python word_count.py tests/TC3.txt
python word_count.py tests/TC4.txt
python word_count.py tests/TC5.txt
```

## Evidencia
Revisar o entregar el archivo:

`p3_wordcount/tests/word_count_results.txt`

### pylint (PEP 8)
```bash
cd /workspaces/A01796384_A4.2
pylint p3_wordcount/word_count.py
```
<img width="1017" height="843" alt="image" src="https://github.com/user-attachments/assets/d0912a17-bb50-4efe-a0e2-4299bb3e122c" />
<img width="860" height="113" alt="image" src="https://github.com/user-attachments/assets/4c51c0f6-143f-4305-ad5a-4d270c68e9bb" />

