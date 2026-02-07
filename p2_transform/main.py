#!/usr/bin/env python3
"""
P2 - Transformación numérica y conversión a BIN/HEX.

Lee enteros (uno por línea). Para cada entero:
1) Calcula un valor transformado (0..255) según el enunciado del problema.
2) Imprime:
   - decimal transformado
   - BIN sin prefijo 0b
   - HEX en mayúsculas sin prefijo 0x
"""

from __future__ import annotations

import argparse


def transform_to_byte(value: int) -> int:
    """
    TODO: Implementar según el enunciado real de P2.
    Debe devolver un entero en [0, 255].
    """
    raise NotImplementedError("Falta implementar la regla del problema P2.")


def to_bin(n: int) -> str:
    return format(n, "b")  # sin 0b


def to_hex(n: int) -> str:
    return format(n, "X")  # mayúsculas, sin 0x


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", required=True, help="Ruta del TC (txt)")
    args = parser.parse_args()

    with open(args.input_path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            original = int(s)
            b = transform_to_byte(original)
            if not 0 <= b <= 255:
                raise ValueError(f"Transform fuera de rango: {b} para {original}")

            print(f"{b} {to_bin(b)} {to_hex(b)}")


if __name__ == "__main__":
    main()
