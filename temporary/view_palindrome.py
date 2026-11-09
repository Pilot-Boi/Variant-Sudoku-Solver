from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    """
    Build an empty puzzle with example Palindrome lines.

    Every mirrored pair avoids sharing a row, column,
    or box, so the example stays solvable as a normal
    Sudoku and doubles as a solver integration check.
    """
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # A straight odd-length line along the diagonal.
    puzzle.add_palindrome([
        (0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
    ])

    # A straight even-length line.
    puzzle.add_palindrome([
        (4, 5), (5, 6), (6, 7), (7, 8),
    ])

    # A bent line.
    puzzle.add_palindrome([
        (6, 3), (7, 4), (7, 5), (6, 6), (5, 5),
    ])

    # Two lines overlapping at their shared center R2C3.
    puzzle.add_palindrome([
        (0, 1), (1, 2), (2, 3),
    ])

    puzzle.add_palindrome([
        (2, 1), (1, 2), (0, 3),
    ])

    return puzzle


if __name__ == "__main__":
    puzzle = create_puzzle()

    show_puzzle(
        puzzle,
        title="Palindrome Sudoku — Visualization Test",
        output="output/palindrome_test.html",
    )
