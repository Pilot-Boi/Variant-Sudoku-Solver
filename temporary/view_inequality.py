from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # Adjacent horizontal inequalities.
    puzzle.add_inequality((0, 0), (0, 1), "<")
    puzzle.add_inequality((0, 2), (0, 1), "<")

    # Adjacent vertical inequalities.
    puzzle.add_inequality((3, 4), (4, 4), "<")
    puzzle.add_inequality((5, 4), (4, 4), "<")

    # A chain of inequalities sharing cells.
    puzzle.add_inequality((7, 1), (7, 2), "<")
    puzzle.add_inequality((7, 2), (7, 3), "<")

    # A nonadjacent inequality drawn as a connector.
    puzzle.add_inequality((2, 7), (5, 7), ">")

    return puzzle


if __name__ == "__main__":
    show_puzzle(
        create_puzzle(),
        title="Inequality Sudoku — Visualization Test",
        output="output/inequality_test.html",
    )
