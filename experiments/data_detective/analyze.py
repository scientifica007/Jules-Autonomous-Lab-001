"""Statistics for invented CSV data, with no external dependencies."""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from statistics import mean, median

FIELDS = {"id", "group", "value"}


def load_rows(csv_path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    seen: set[str] = set()
    with csv_path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None or set(reader.fieldnames) != FIELDS:
            raise ValueError("CSV must contain exactly these columns: id, group, value")
        for number, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"Row {number}: too many fields")
            item_id = (row["id"] or "").strip()
            group = (row["group"] or "").strip()
            if not item_id or not group:
                raise ValueError(f"Row {number}: empty id or group")
            if item_id in seen:
                raise ValueError(f"Row {number}: duplicate id '{item_id}'")
            seen.add(item_id)
            try:
                value = float(row["value"] or "")
            except ValueError as exc:
                raise ValueError(f"Row {number}: invalid number") from exc
            if not math.isfinite(value):
                raise ValueError(f"Row {number}: non-finite number")
            rows.append({"id": item_id, "group": group, "value": value})
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    vals = [float(row["value"]) for row in rows]
    groups = sorted({str(row["group"]) for row in rows})
    return {
        "count": len(vals),
        "groups": groups,
        "min": min(vals) if vals else None,
        "max": max(vals) if vals else None,
        "mean": mean(vals) if vals else None,
        "median": median(vals) if vals else None,
    }


# TODO(Jules): add optional human-readable output without changing the default JSON API.

def main() -> None:
    parser = argparse.ArgumentParser(description="Offline synthetic-data CSV analyzer")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(summarize(load_rows(args.csv_path)), indent=2, ensure_ascii=False))
    except (OSError, ValueError) as error:
        parser.exit(2, f"Analysis error: {error}\n")


if __name__ == "__main__":
    main()
