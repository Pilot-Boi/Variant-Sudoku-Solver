"""View any discovered Sudoku puzzle as HTML.

Examples:
    python view_puzzle.py ctc_005
    python view_puzzle.py ctc_005 --solve
    python view_puzzle.py killer_001
    python view_puzzle.py --list
"""
import argparse
import importlib
import pkgutil
from pathlib import Path

import puzzles
from visualization.html_renderer import show_puzzle


def discover_viewable_puzzles():
    """Return {short_module_name: (full_module_path, module)}."""
    found = {}
    for info in pkgutil.walk_packages(puzzles.__path__, prefix="puzzles."):
        if info.ispkg or info.name.rsplit(".", 1)[-1].startswith("_"):
            continue
        module = importlib.import_module(info.name)
        if not callable(getattr(module, "create_puzzle", None)):
            continue
        short_name = info.name.rsplit(".", 1)[-1]
        if short_name in found:
            raise ValueError(
                f"Duplicate puzzle module basename {short_name!r}: "
                f"{found[short_name][0]} and {info.name}. "
                "Use distinct filenames for puzzle modules."
            )
        found[short_name] = (info.name, module)
    return dict(sorted(found.items()))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("puzzle", nargs="?", help="Puzzle module name, e.g. ctc_005")
    parser.add_argument("--solve", action="store_true", help="Solve and display the solution")
    parser.add_argument("--list", action="store_true", help="List available puzzle modules")
    parser.add_argument("--output", type=Path, help="Custom HTML output path")
    args = parser.parse_args(argv)

    registry = discover_viewable_puzzles()
    if args.list:
        for short_name, (module_path, module) in registry.items():
            print(f"{short_name:25} {getattr(module, 'NAME', module_path)}")
        return

    if not args.puzzle:
        parser.error("provide a puzzle module name, or use --list")

    selection = args.puzzle.removeprefix("puzzles.")
    if selection in registry:
        module = registry[selection][1]
        short_name = selection
    else:
        matches = [(short, module) for short, (path, module) in registry.items()
                   if path == f"puzzles.{selection}"]
        if not matches:
            parser.error(f"unknown puzzle {args.puzzle!r}; use --list to see available puzzles")
        short_name, module = matches[0]

    name = getattr(module, "NAME", short_name)
    puzzle = module.create_puzzle()
    output = args.output or Path("output") / f"{short_name}.html"

    if not args.solve:
        path = show_puzzle(puzzle, title=name, output=str(output))
        print(f"Puzzle visualization saved to: {path}")
        return

    print(f"Solving {name}...")
    status, solutions, solver = puzzle.check_uniqueness()
    if not solutions:
        print("No solution found. Opening unsolved puzzle instead.")
        path = show_puzzle(puzzle, title=f"{name} (Unsolved)", output=str(output))
    else:
        solution = solutions[0]
        solution_grid = [[solution[(r, c)] for c in range(9)] for r in range(9)]
        path = show_puzzle(puzzle, title=name, output=str(output), solution=solution_grid)
    print(f"Puzzle status: {status}")
    print(f"Search decisions: {solver.nodes}")
    print(f"Backtracks: {solver.backtracks}")
    print(f"Puzzle visualization saved to: {path}")


if __name__ == "__main__":
    main()
