
from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def main():
    # Create an empty 9x9 Sudoku grid.
    empty_grid = [
        [0 for _ in range(9)]
        for _ in range(9)
    ]

    puzzle = SudokuPuzzle(empty_grid)
    puzzle.add_diagonal_constraints()

    show_puzzle(
        puzzle,
        title="Diagonal Visualization Test",
        output="output/diagonal_test.html"
    )


if __name__ == "__main__":
    main()
