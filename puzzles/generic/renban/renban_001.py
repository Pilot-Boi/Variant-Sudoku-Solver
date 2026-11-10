
    
  
from sudoku.puzzle import SudokuPuzzle

NAME = "Renban Sudoku #001"


def create_puzzle():
    # 0 denotes an empty cell. Coordinates for lines are zero-based.
    grid = [
        [0, 3, 5, 1, 0, 9, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [2, 0, 0, 0, 0, 3, 9, 1, 4],
        [0, 0, 0, 4, 6, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [5, 0, 0, 0, 7, 8, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 6, 0, 4, 0, 5, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    # Top-left short vertical line.
    puzzle.add_renban([(0, 1), (1, 1)])

    # Upper-left bent line.
    puzzle.add_renban([(1, 3), (2, 3), (2, 2)])

    # Upper-middle bent line.
    puzzle.add_renban([(1, 4), (2, 4), (3, 4), (3, 3), (3, 2)])

    # Upper-right diagonal zigzag.
    puzzle.add_renban([(1, 5), (2, 6), (1, 7), (0, 8)])

    # Short vertical line on the right.
    puzzle.add_renban([(1, 8), (2, 8)])

    # Upper-middle-right L-shaped line.
    puzzle.add_renban([(2, 5), (3, 5), (3, 6)])

    # Short horizontal line on the left.
    puzzle.add_renban([(3, 0), (3, 1)])

    # Long left-edge vertical line.
    puzzle.add_renban([(4, 0), (5, 0), (6, 0), (7, 0), (8, 0)])

    # Lower-left diagonal zigzag.
    puzzle.add_renban([(4, 2), (5, 1), (6, 2), (7, 3)])

    # Right-edge bent line.
    puzzle.add_renban([(3, 8), (4, 8), (5, 8), (5, 7), (5, 6)])

    # Lower-middle horizontal line.
    puzzle.add_renban([(6, 3), (6, 4), (6, 5)])

    # Lower-right hooked line.
    puzzle.add_renban([(6, 6), (6, 7), (7, 7), (8, 7)])

    # Lower-right short vertical line.
    puzzle.add_renban([(6, 8), (7, 8)])

    # Bottom-center diagonal line.
    puzzle.add_renban([(7, 5), (8, 4)])

    # Bottom-center-right bent line.
    puzzle.add_renban([(8, 5), (8, 6), (7, 6)])

    return puzzle