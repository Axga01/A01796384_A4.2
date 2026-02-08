#!/usr/bin/env python3
"""
P1 - Estadísticos descriptivos.
Lee una lista de números (uno por línea) y calcula:
n, mean, median, mode, std dev (muestral), variance (muestral), min, max.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter
from typing import List


def read_numbers(path: str) -> List[float]:
    numbers: List[float] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            try:
                numbers.append(float(s))
            except ValueError:
                continue  # ignora líneas que no son números
    return numbers


def mean(values: List[float]) -> float:
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 1:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0


def mode(values: List[float]) -> float:
    counts = Counter(values)
    max_freq = max(counts.values())
    modes = [v for v, c in counts.items() if c == max_freq]
    return min(modes)


def sample_variance(values: List[float]) -> float:
    n = len(values)
    if n < 2:
        return 0.0
    mu = mean(values)
    return sum((x - mu) ** 2 for x in values) / (n - 1)


def sample_std(values: List[float]) -> float:
    return math.sqrt(sample_variance(values))


def fmt(x: float) -> str:
    if float(x).is_integer():
        return str(int(x))
    return f"{x:.8f}".rstrip("0").rstrip(".")


def save_results(output_path: str, title: str, results: str) -> None:
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"\n===== {title} =====\n")
        f.write(results)
        f.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", required=True, help="Ruta del TC (txt)")
    args = parser.parse_args()

    values = read_numbers(args.input_path)

    n = len(values)
    mu = mean(values)
    med = median(values)
    mod = mode(values)
    std = sample_std(values)
    var = sample_variance(values)
    mn = min(values)
    mx = max(values)

    output = f"""n: {n}
Mean: {fmt(mu)}
Median: {fmt(med)}
Mode: {fmt(mod)}
Std dev: {fmt(std)}
Variance: {fmt(var)}
Min: {fmt(mn)}
Max: {fmt(mx)}
"""

    print(output)

    test_name = args.input_path.split("/")[-1].replace(".txt", "")

    save_results(
        "p1_stats/tests/A4.2.P1.Results.txt",
        test_name,
        output
    )


if __name__ == "__main__":
    main()
