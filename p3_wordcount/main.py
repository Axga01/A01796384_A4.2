#!/usr/bin/env python3
"""
P3 - Conteo de palabras.
Lee palabras (una por línea) y muestra "palabra conteo" ordenado alfabéticamente.
"""

from __future__ import annotations

import argparse
from collections import Counter


def read_words(path: str) -> list[str]:
    words: list[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w:
                words.append(w)
    if not words:
        raise ValueError("El archivo no contiene palabras.")
    return words


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", required=True, help="Ruta del TC (txt)")
    args = parser.parse_args()

    words = read_words(args.input_path)
    counts = Counter(words)

    for w in sorted(counts.keys()):
        print(f"{w} {counts[w]}")


if __name__ == "__main__":
    main()
