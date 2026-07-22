"""Validate notebook JSON and execute canonical teacher notebooks in order."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGETS = [
    ROOT / "course_v2/lessons/lesson01_first_analysis/lesson01_learning.ipynb",
    ROOT / "course_v2/lessons/lesson01_first_analysis/lesson01_solutions.ipynb",
    ROOT / "course_v2/lessons/lesson02_python_basics/lesson02_learning.ipynb",
    ROOT / "course_v2/lessons/lesson02_python_basics/lesson02_solutions.ipynb",
    ROOT / "course_v2/lessons/lesson03_conditions/lesson03_learning.ipynb",
    ROOT / "course_v2/lessons/lesson03_conditions/lesson03_solutions.ipynb",
    ROOT / "course_v2/lessons/lesson04_list_tuple/lesson04_learning.ipynb",
    ROOT / "course_v2/lessons/lesson04_list_tuple/lesson04_solutions.ipynb",
    ROOT / "course_v2/lessons/lesson05_dict_set/lesson05_learning.ipynb",
    ROOT / "course_v2/lessons/lesson05_dict_set/lesson05_solutions.ipynb",
    ROOT / "course_v2/lessons/lesson06_for_loops/lesson06_learning.ipynb",
    ROOT / "course_v2/lessons/lesson06_for_loops/lesson06_solutions.ipynb",
]


def validate(path: Path, execute: bool) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["nbformat"] == 4, f"{path}: unsupported notebook format"
    assert data["cells"], f"{path}: notebook is empty"

    if not execute:
        return

    namespace = {"__name__": "__notebook__", "display": lambda value: value}
    for index, cell in enumerate(data["cells"], start=1):
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        try:
            exec(compile(source, f"{path.name}:cell-{index}", "exec"), namespace)
        except Exception as exc:
            raise RuntimeError(f"{path}: cell {index} failed") from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--structure-only", action="store_true")
    args = parser.parse_args()
    os.chdir(ROOT)
    for target in TARGETS:
        # Solutions are intentionally absent from the student repository until
        # the instructor publishes them after class.
        if not target.exists():
            print(f"SKIP {target.relative_to(ROOT)} (not published)")
            continue
        validate(target, execute=not args.structure_only)
        print(f"PASS {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
