from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # A straight Between Line.
    puzzle.add_between_line([
        (1, 1), (1, 2), (1, 3), (1, 4),
    ])

    # A bent line with diagonal connections.
    puzzle.add_between_line([
        (3, 6), (4, 7), (5, 7), (6, 6),
    ])

    # Two lines overlapping at R7C3.
    puzzle.add_between_line([
        (5, 1), (6, 2), (6, 3), (7, 4),
    ])

    puzzle.add_between_line([
        (8, 1), (7, 2), (6, 3), (5, 4),
    ])

    return puzzle


if __name__ == "__main__":
    show_puzzle(
        create_puzzle(),
        title="Between Lines — Visualization Test",
        output="output/between_test.html",
    )
