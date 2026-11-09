from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    """
    Build an empty puzzle with example arrows.

    Geometries avoid forcing impossible sums, so the
    example also works as a solver integration check.
    """
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # A short straight arrow.
    puzzle.add_arrow(
        [(0, 0)],
        [(0, 1), (0, 2)],
    )

    # A longer bent arrow.
    puzzle.add_arrow(
        [(2, 2)],
        [(3, 2), (4, 1), (5, 0), (6, 1)],
    )

    # Two arrows overlapping at R2C7.
    puzzle.add_arrow(
        [(0, 5)],
        [(1, 6), (2, 6)],
    )

    puzzle.add_arrow(
        [(0, 7)],
        [(1, 6), (2, 5)],
    )

    # A two-cell circle read as a two-digit number.
    puzzle.add_arrow(
        [(7, 0), (8, 0)],
        [(8, 1), (7, 2), (8, 3), (7, 4)],
    )

    return puzzle


if __name__ == "__main__":
    puzzle = create_puzzle()

    show_puzzle(
        puzzle,
        title="Arrow Sudoku — Visualization Test",
        output="output/arrow_test.html",
    )
