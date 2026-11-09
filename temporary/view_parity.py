from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def create_puzzle():
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)

    # A cluster of odd cells.
    puzzle.add_odd_cell((1, 1))
    puzzle.add_odd_cell((1, 2))
    puzzle.add_odd_cell((2, 1))

    # A cluster of even cells.
    puzzle.add_even_cell((4, 4))
    puzzle.add_even_cell((4, 5))
    puzzle.add_even_cell((5, 4))

    # Scattered parity cells.
    puzzle.add_odd_cell((7, 7))
    puzzle.add_even_cell((7, 1))
    puzzle.add_odd_cell((0, 8))
    puzzle.add_even_cell((8, 0))

    return puzzle


if __name__ == "__main__":
    show_puzzle(
        create_puzzle(),
        title="Odd/Even Sudoku — Visualization Test",
        output="output/parity_test.html",
    )
