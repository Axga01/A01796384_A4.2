#!/usr/bin/env python3
"""
P3 - Word Count.

Reads a text file and counts the frequency of each distinct word.

Requirements covered:
- Command line execution: python wordCount.py file.txt
- Uses basic algorithms (no counting libraries)
- Handles invalid lines and continues execution
- Prints results to screen and saves to WordCountResults.txt
- Includes elapsed execution time
- PEP 8 compliant
"""

from __future__ import annotations

import argparse
import os
import time
from typing import Dict


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_FILENAME = os.path.join(SCRIPT_DIR, "tests", "WordCountResults.txt")


def normalize_word(word: str) -> str:
    """Normalize word: lowercase and remove punctuation."""
    cleaned = ""
    for char in word:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned


def read_words(path: str) -> Dict[str, int]:
    """
    Read words from file and count frequency using basic algorithm.
    Invalid data is ignored and execution continues.
    """
    frequencies: Dict[str, int] = {}

    with open(path, "r", encoding="utf-8") as file:
        for lineno, line in enumerate(file, start=1):
            raw_words = line.strip().split()

            if not raw_words:
                print(f"Warning (line {lineno}): empty line ignored")
                continue

            for raw_word in raw_words:
                word = normalize_word(raw_word)

                if word == "":
                    continue

                if word in frequencies:
                    frequencies[word] += 1
                else:
                    frequencies[word] = 1

    return frequencies


def build_output(input_path: str, frequencies: Dict[str, int], elapsed: float) -> str:
    """Build console/file output."""
    base_name = os.path.basename(input_path)

    output = f"Input file: {base_name}\n"
    output += "Word frequencies:\n"

    for word in sorted(frequencies):
        output += f"{word}: {frequencies[word]}\n"

    output += f"Elapsed time (s): {elapsed:.8f}\n"

    return output


def append_results(output_text: str) -> None:
    """Save results into WordCountResults.txt (append mode)."""
    os.makedirs(os.path.dirname(RESULTS_FILENAME), exist_ok=True)

    with open(RESULTS_FILENAME, "a", encoding="utf-8") as file:
        file.write("\n===== RUN =====\n")
        file.write(output_text)


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        prog="wordCount.py",
        description="Count word frequency from a text file.",
    )
    parser.add_argument("input_path", help="Path to input text file")
    return parser.parse_args()


def main() -> None:
    """Program entry point."""
    args = parse_args()

    start = time.perf_counter()
    frequencies = read_words(args.input_path)
    elapsed = time.perf_counter() - start

    if not frequencies:
        output_text = (
            f"Input file: {os.path.basename(args.input_path)}\n"
            "No valid words found.\n"
            f"Elapsed time (s): {elapsed:.8f}\n"
        )
        print(output_text)
        append_results(output_text)
        return

    output_text = build_output(args.input_path, frequencies, elapsed)

    print(output_text)
    append_results(output_text)


if __name__ == "__main__":
    main()
