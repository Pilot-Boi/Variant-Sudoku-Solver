from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import render_puzzle, show_puzzle


def create_puzzle(include_negative=False):
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # Horizontal markers.
    puzzle.add_xv((0, 1), (0, 2), "V")
    puzzle.add_xv((0, 4), (0, 5), "X")

    # Vertical markers.
    puzzle.add_xv((3, 2), (4, 2), "X")
    puzzle.add_xv((6, 6), (7, 6), "V")

    # Markers sharing a cell.
    puzzle.add_xv((4, 4), (4, 5), "V")
    puzzle.add_xv((4, 5), (5, 5), "X")

    # A marker crossing a 3x3 box boundary.
    puzzle.add_xv((8, 2), (8, 3), "X")

    if include_negative:
        puzzle.add_negative_xv_constraints()

    return puzzle


if __name__ == "__main__":
    show_puzzle(
        create_puzzle(),
        title="XV Sudoku — Visualization Test",
        output="output/xv_test.html",
    )

    # Rendered without opening a browser; used to test
    # inspector behavior with negative constraints.
    render_puzzle(
        create_puzzle(include_negative=True),
        title="XV Sudoku — Negative Constraints Test",
        output="output/xv_negative_test.html",
    )
