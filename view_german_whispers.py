from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # A winding line with diagonal connections.
    puzzle.add_german_whispers([
        (1, 1), (2, 2), (2, 3), (1, 4), (2, 5),
    ])

    # A straight horizontal line.
    puzzle.add_german_whispers([
        (5, 1), (5, 2), (5, 3), (5, 4),
    ])

    # Overlaps the horizontal line at R6C4.
    puzzle.add_german_whispers([
        (7, 3), (6, 3), (5, 3), (4, 4),
    ])

    return puzzle


if __name__ == "__main__":
    puzzle = create_puzzle()

    show_puzzle(
        puzzle,
        title="German Whispers Sudoku — Visualization Test",
        output="output/german_whispers_test.html",
    )
