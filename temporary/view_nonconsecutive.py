
from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)
    puzzle.add_nonconsecutive_constraints()

    return puzzle


if __name__ == "__main__":
    puzzle = create_puzzle()

    show_puzzle(
        puzzle,
        title="Nonconsecutive Sudoku — Visualization Test",
        output="output/nonconsecutive_test.html",
    )
