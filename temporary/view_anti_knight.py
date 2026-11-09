from sudoku.puzzle import SudokuPuzzle
from visualization.html_renderer import show_puzzle


def main():
    grid = [[0] * 9 for _ in range(9)]

    puzzle = SudokuPuzzle(grid)
    puzzle.add_anti_knight_constraints()

    show_puzzle(
        puzzle,
        title="Anti-Knight Sudoku — Visualization Test",
        output="output/anti_knight_test.html",
    )


if __name__ == "__main__":
    main()