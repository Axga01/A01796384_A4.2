#!/usr/bin/env python3
"""
P2 - Converter (Binary & Hex).

Reads a text file with one integer per line and converts each valid integer
to binary and hexadecimal using basic algorithms (no bin/hex/format).

Requirements covered:
- CLI invocation: python convert_numbers.py fileWithData.txt
- Converts to binary and hexadecimal (basic algorithm, no helper functions)
- Handles invalid data: prints warning and continues
- Prints results to screen and saves them to convertion_results.txt
- Includes elapsed time on screen and in results file
- PEP 8 compliant (note: filename required by assignment)
"""

# pylint: disable=invalid-name

from __future__ import annotations

import argparse
import os
import time
from typing import List, Tuple


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_PATH = os.path.join(SCRIPT_DIR, "tests", "convertion_results.txt")
DIGITS = "0123456789ABCDEF"


def read_integers(path: str) -> List[int]:
    """
    Read integers from a file (one per line).

    Invalid lines are reported in the console and ignored (execution continues).
    """
    values: List[int] = []
    with open(path, "r", encoding="utf-8") as file:
        for lineno, line in enumerate(file, start=1):
            raw = line.strip()

            if raw == "":
                print(f"Warning (line {lineno}): empty line ignored")
                continue

            try:
                # We expect integers for base conversion.
                values.append(int(raw))
            except ValueError:
                print(f"Warning (line {lineno}): invalid integer '{raw}' ignored")
                continue

    return values


def to_base(number: int, base: int) -> str:
    """
    Convert an integer to a base-N string using repeated division.

    This is a basic algorithm implementation (no bin/hex/format).
    """
    if number == 0:
        return "0"

    sign = ""
    n = number
    if n < 0:
        sign = "-"
        n = -n

    chars: List[str] = []
    while n > 0:
        remainder = n % base
        chars.append(DIGITS[remainder])
        n //= base

    chars.reverse()
    return sign + "".join(chars)


def build_output(input_path: str, rows: List[Tuple[int, str, str]], elapsed: float) -> str:
    """Build output text for console/file."""
    base_name = os.path.basename(input_path)
    lines: List[str] = [
        f"Input file: {base_name}",
        "Number | Binary | Hex",
        "-" * 60,
    ]

    for num, b_str, h_str in rows:
        lines.append(f"{num} | {b_str} | {h_str}")

    lines.append("-" * 60)
    lines.append(f"Elapsed time (s): {elapsed:.6f}")
    lines.append("")  # trailing newline

    return "\n".join(lines)


def append_results(output_text: str) -> None:
    """Append results to ConvertionResults.txt inside p2_transform/tests/."""
    os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)
    with open(RESULTS_PATH, "a", encoding="utf-8") as file:
        file.write("\n===== RUN =====\n")
        file.write(output_text)


def parse_args() -> argparse.Namespace:
    """Parse CLI args (minimum required invocation)."""
    parser = argparse.ArgumentParser(
        prog="convertNumbers.py",
        description="Convert integers to binary and hexadecimal from a file.",
    )
    parser.add_argument("input_path", help="Path to input .txt file (one integer per line)")
    return parser.parse_args()


def main() -> None:
    """Program entry point."""
    args = parse_args()

    start = time.perf_counter()
    values = read_integers(args.input_path)

    if not values:
        elapsed = time.perf_counter() - start
        output_text = (
            f"Input file: {os.path.basename(args.input_path)}\n"
            "Error: no valid integer data found. Nothing to convert.\n"
            f"Elapsed time (s): {elapsed:.6f}\n"
        )
        print(output_text)
        append_results(output_text)
        return

    rows: List[Tuple[int, str, str]] = []
    for n in values:
        bin_str = to_base(n, 2)
        hex_str = to_base(n, 16)
        rows.append((n, bin_str, hex_str))

    elapsed = time.perf_counter() - start
    output_text = build_output(args.input_path, rows, elapsed)

    print(output_text)
    append_results(output_text)


if __name__ == "__main__":
    main()
