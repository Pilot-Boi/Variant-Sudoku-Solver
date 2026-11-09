from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # A full-length diagonal built from an outside clue.
    cells = SudokuPuzzle.little_killer_cells(
        (-1, -1), "down-right"
    )
    puzzle.add_little_killer(cells, 45)

    # A short diagonal entering from the top edge.
    cells = SudokuPuzzle.little_killer_cells(
        (-1, 6), "down-right"
    )
    puzzle.add_little_killer(cells, 12)

    # A diagonal from the right edge, heading up-left.
    cells = SudokuPuzzle.little_killer_cells(
        (5, 9), "up-left"
    )
    puzzle.add_little_killer(cells, 30)

    # A manually specified short diagonal.
    puzzle.add_little_killer(
        [(8, 2), (7, 1), (6, 0)], 15
    )

    return puzzle


if __name__ == "__main__":
    show_puzzle(
        create_puzzle(),
        title="Little Killer — Visualization Test",
        output="output/little_killer_test.html",
    )
