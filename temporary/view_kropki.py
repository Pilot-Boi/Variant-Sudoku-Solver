from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import render_puzzle, show_puzzle


def create_puzzle(include_negative=False):
    """
    Build an empty puzzle with example Kropki dots.

    include_negative: also add negative Kropki
    constraints to every undotted orthogonal pair.
    """
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # Horizontal white dots. The chain R1C2-R1C3 (white)
    # and R1C3-R1C4 (black) can resolve as 1-2-4,
    # showing that 1 and 2 satisfy both dot types.
    puzzle.add_kropki_dot((0, 1), (0, 2), "white")
    puzzle.add_kropki_dot((0, 2), (0, 3), "black")

    # Vertical white dot.
    puzzle.add_kropki_dot((2, 5), (3, 5), "white")

    # Vertical black dot.
    puzzle.add_kropki_dot((4, 7), (5, 7), "black")

    # White dot crossing a 3x3 box boundary.
    puzzle.add_kropki_dot((4, 2), (4, 3), "white")

    # Black dot crossing a 3x3 box boundary.
    puzzle.add_kropki_dot((5, 4), (6, 4), "black")

    # A few extra dots inside boxes.
    puzzle.add_kropki_dot((7, 1), (8, 1), "white")
    puzzle.add_kropki_dot((8, 5), (8, 6), "black")

    if include_negative:
        puzzle.add_negative_kropki_constraints()

    return puzzle


if __name__ == "__main__":
    show_puzzle(
        create_puzzle(),
        title="Kropki Sudoku — Visualization Test",
        output="output/kropki_test.html",
    )

    # Rendered without opening a browser; used to test
    # inspector behavior with negative constraints.
    render_puzzle(
        create_puzzle(include_negative=True),
        title="Kropki Sudoku — Negative Constraints Test",
        output="output/kropki_negative_test.html",
    )
