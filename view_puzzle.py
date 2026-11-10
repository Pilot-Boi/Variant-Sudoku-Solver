
import argparse

from puzzles.ctc_005 import NAME, create_puzzle
from visualization.html_renderer import show_puzzle


def main():
    parser = argparse.ArgumentParser(
        description="View a Sudoku puzzle, optionally with its solution."
    )

    parser.add_argument(
        "--solve",
        action="store_true",
        help="Solve the puzzle and display its solution."
    )

    args = parser.parse_args()

    puzzle = create_puzzle()

    # Default behavior: display the unsolved puzzle.
    if not args.solve:
        path = show_puzzle(
            puzzle,
            title=NAME,
            output="output/ctc_001.html"
        )

        print(f"Puzzle visualization saved to: {path}")
        return

    # Optional behavior: attempt to solve the puzzle.
    print("Solving puzzle...")

    status, solutions, solver = puzzle.check_uniqueness()

    if not solutions:
        print("No solution found. Opening unsolved puzzle instead.")

        path = show_puzzle(
            puzzle,
            title=f"{NAME} (Unsolved)",
            output="output/ctc_001.html"
        )

        print(f"Puzzle visualization saved to: {path}")
        return

    solution = solutions[0]

    solution_grid = [
        [solution[(r, c)] for c in range(9)]
        for r in range(9)
    ]

    path = show_puzzle(
        puzzle,
        title=NAME,
        output="output/ctc_003.html",
        solution=solution_grid
    )

    print(f"Puzzle status: {status}")
    print(f"Search decisions: {solver.nodes}")
    print(f"Backtracks: {solver.backtracks}")
    print(f"Puzzle visualization saved to: {path}")


if __name__ == "__main__":
    main()