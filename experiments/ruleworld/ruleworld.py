"""Small, dependency-free and deterministic 2D cellular automaton (B3/S23)."""
from __future__ import annotations

import argparse
import json
from collections import Counter

PATTERNS = {
    "block": {(1, 1), (2, 1), (1, 2), (2, 2)},
    "blinker": {(1, 2), (2, 2), (3, 2)},
    "glider": {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)},
}


def evolve(live: set[tuple[int, int]], width: int, height: int, wrap: bool = False) -> set[tuple[int, int]]:
    """Return next generation on a finite or wrapping grid."""
    if width < 1 or height < 1:
        raise ValueError("width and height must be positive")
    if any(not (0 <= x < width and 0 <= y < height) for x, y in live):
        raise ValueError("live cells must be inside the grid")
    counts: Counter[tuple[int, int]] = Counter()
    for x, y in live:
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == dy == 0:
                    continue
                candidate = x + dx, y + dy
                if wrap:
                    candidate = candidate[0] % width, candidate[1] % height
                    counts[candidate] += 1
                elif 0 <= candidate[0] < width and 0 <= candidate[1] < height:
                    counts[candidate] += 1
    return {position for position, neighbors in counts.items()
            if neighbors == 3 or (neighbors == 2 and position in live)}


# TODO(Jules): offer optional bounded detection of repeating states (e.g., period-two blinker).

def simulate(pattern: str, width: int, height: int, steps: int, wrap: bool = False) -> list[set[tuple[int, int]]]:
    if pattern not in PATTERNS:
        raise ValueError(f"Unknown pattern: {pattern}")
    if steps < 0:
        raise ValueError("steps must be non-negative")
    live = set(PATTERNS[pattern])
    if any(x >= width or y >= height for x, y in live):
        raise ValueError("Selected pattern does not fit the grid")
    history = [live]
    for _ in range(steps):
        live = evolve(live, width, height, wrap)
        history.append(live)
    return history


def render(live: set[tuple[int, int]], width: int, height: int) -> str:
    return "\n".join("".join("#" if (x, y) in live else "." for x in range(width))
                     for y in range(height))


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline deterministic cellular automaton")
    parser.add_argument("--pattern", choices=sorted(PATTERNS), default="glider")
    parser.add_argument("--width", type=int, default=12)
    parser.add_argument("--height", type=int, default=12)
    parser.add_argument("--steps", type=int, default=4)
    parser.add_argument("--format", choices=("ascii", "json"), default="ascii")
    parser.add_argument("--wrap", action="store_true", help="Enable toroidal wrapping boundaries")
    args = parser.parse_args()
    try:
        history = simulate(args.pattern, args.width, args.height, args.steps, args.wrap)
    except ValueError as error:
        parser.error(str(error))
    if args.format == "json":
        print(json.dumps({"pattern": args.pattern, "width": args.width,
                          "height": args.height, "steps": args.steps,
                          "population": [len(state) for state in history],
                          "final_cells": [list(cell) for cell in sorted(history[-1])]},
                         indent=2))
    else:
        for index, state in enumerate(history):
            print(f"Generation {index} ({len(state)} live cells)\n{render(state, args.width, args.height)}\n")


if __name__ == "__main__":
    main()
