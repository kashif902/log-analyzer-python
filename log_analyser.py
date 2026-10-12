import sys
from collections import Counter


LEVELS = ("ERROR", "WARNING", "INFO", "DEBUG")


def analyze_log(log_path):
    counts = Counter({level: 0 for level in LEVELS})
    error_lines = []

    with open(log_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            for level in LEVELS:
                if level in line:
                    counts[level] += 1
            if "ERROR" in line:
                error_lines.append(line.rstrip("\n"))

    return counts, error_lines


def main():
    arguments = sys.argv[1:]
    show_errors = "--errors" in arguments
    paths = [argument for argument in arguments if argument != "--errors"]

    if len(paths) != 1:
        print("Usage: py log_analyser.py <log_file> [--errors]")
        return

    log_path = paths[0]
    try:
        counts, error_lines = analyze_log(log_path)
    except FileNotFoundError:
        print(f"File not found: {log_path}")
        return

    for level in LEVELS:
        print(f"{level}: {counts[level]}")

    if show_errors:
        print("ERROR lines:")
        for line in error_lines:
            print(line)


if __name__ == "__main__":
    main()