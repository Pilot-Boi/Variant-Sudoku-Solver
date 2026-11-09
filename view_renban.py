from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # A straight horizontal line.
    puzzle.add_renban([
        (1, 1), (1, 2), (1, 3), (1, 4),
    ])

    # A bent line with a diagonal connection.
    puzzle.add_renban([
        (3, 6), (4, 6), (5, 7), (5, 8),
    ])

    # Two lines overlapping at R7C3.
    puzzle.add_renban([
        (6, 1), (6, 2), (6, 3), (7, 3),
    ])

    puzzle.add_renban([
        (8, 2), (7, 3), (8, 4),
    ])

    return puzzle


if __name__ == "__main__":
    puzzle = create_puzzle()

    show_puzzle(
        puzzle,
        title="Renban Sudoku — Visualization Test",
        output="output/renban_test.html",
    )
