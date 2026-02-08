#!/usr/bin/env python3
"""
P1 - Estadísticos descriptivos.

Lee una lista de números (uno por línea) desde un archivo de texto y calcula:
n, mean, median, mode, std dev (muestral), variance (muestral), min, max.

Requisitos cubiertos:
- Se invoca desde línea de comandos con el archivo como parámetro:
  python compute_statistics.py fileWithData.txt
- Calcula estadísticas con algoritmos básicos (sin librerías de estadística).
- Maneja datos inválidos: muestra error en consola y continúa.
- Imprime resultados en pantalla y los guarda en statistics_results.txt
- Incluye el tiempo transcurrido en pantalla y en el archivo de resultados.
- Cumple PEP 8.
"""

from __future__ import annotations

import argparse
import os
import time
from typing import Dict, List, Tuple


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_FILENAME = os.path.join(SCRIPT_DIR, "tests", "statistics_results.txt")


StatsTuple = Tuple[int, float, float, float, float, float, float, float]


def fmt(number: float) -> str:
    """Format numbers without scientific notation and with up to 8 decimals."""
    if float(number).is_integer():
        return str(int(number))
    return f"{number:.8f}".rstrip("0").rstrip(".")


def read_numbers(path: str) -> List[float]:
    """
    Read numeric values from a text file.

    Invalid lines are reported in the console and ignored (execution continues).
    """
    values: List[float] = []
    with open(path, "r", encoding="utf-8") as file:
        for lineno, line in enumerate(file, start=1):
            raw = line.strip()

            if raw == "":
                print(f"Warning (line {lineno}): empty line ignored")
                continue

            try:
                values.append(float(raw))
            except ValueError:
                print(f"Warning (line {lineno}): invalid number '{raw}' ignored")
    return values


def mean(values: List[float]) -> float:
    """Compute arithmetic mean."""
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    """Compute median."""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 1:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0


def mode(values: List[float]) -> float:
    """
    Compute mode using a basic frequency dictionary.

    If there is a tie, returns the smallest value (deterministic behavior).
    """
    freq: Dict[float, int] = {}
    for value in values:
        freq[value] = freq.get(value, 0) + 1

    max_freq = 0
    best_values: List[float] = []

    for value, count in freq.items():
        if count > max_freq:
            max_freq = count
            best_values = [value]
        elif count == max_freq:
            best_values.append(value)

    return min(best_values)


def sample_variance(values: List[float]) -> float:
    """Compute sample variance (n-1). Returns 0.0 if n < 2."""
    n = len(values)
    if n < 2:
        return 0.0

    mu = mean(values)
    total = 0.0
    for x in values:
        total += (x - mu) ** 2

    return total / (n - 1)


def sample_std(values: List[float]) -> float:
    """Compute sample standard deviation (sqrt of sample variance)."""
    var = sample_variance(values)
    return var ** 0.5


def compute_stats(values: List[float]) -> StatsTuple:
    """Compute all required descriptive statistics."""
    n = len(values)
    mu = mean(values)
    med = median(values)
    mod = mode(values)
    std = sample_std(values)
    var = sample_variance(values)
    mn = min(values)
    mx = max(values)
    return n, mu, med, mod, std, var, mn, mx


def build_output(input_path: str, stats: StatsTuple, elapsed_seconds: float) -> str:
    """Build the output string for console and file."""
    n, mu, med, mod, std, var, mn, mx = stats
    base_name = os.path.basename(input_path)

    return (
        f"Input file: {base_name}\n"
        f"n: {n}\n"
        f"Mean: {fmt(mu)}\n"
        f"Median: {fmt(med)}\n"
        f"Mode: {fmt(mod)}\n"
        f"Std dev: {fmt(std)}\n"
        f"Variance: {fmt(var)}\n"
        f"Min: {fmt(mn)}\n"
        f"Max: {fmt(mx)}\n"
        f"Elapsed time (s): {fmt(elapsed_seconds)}\n"
    )


def append_results(output_text: str) -> None:
    """
    Append results to statistics_results.txt.

    Using append lets you run multiple test cases and keep evidence in one file.
    """
    os.makedirs(os.path.dirname(RESULTS_FILENAME), exist_ok=True)
    with open(RESULTS_FILENAME, "a", encoding="utf-8") as file:
        file.write("\n===== RUN =====\n")
        file.write(output_text)


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments (minimal invocation required by instructions)."""
    parser = argparse.ArgumentParser(
        prog="compute_statistics.py",
        description="Compute descriptive statistics from a file (one number per line).",
    )
    parser.add_argument(
        "input_path",
        help="Path to input .txt file with one number per line",
    )
    return parser.parse_args()


def main() -> None:
    """Program entry point."""
    args = parse_args()

    start = time.perf_counter()
    values = read_numbers(args.input_path)
    elapsed = time.perf_counter() - start

    if not values:
        output_text = (
            f"Input file: {os.path.basename(args.input_path)}\n"
            "Error: no valid numeric data found. Nothing to compute.\n"
            f"Elapsed time (s): {fmt(elapsed)}\n"
        )
        print(output_text)
        append_results(output_text)
        return

    stats = compute_stats(values)
    output_text = build_output(args.input_path, stats, elapsed)

    print(output_text)
    append_results(output_text)


if __name__ == "__main__":
    main()
