
    
  
"""Arrow Sudoku #001, transcribed from the supplied puzzle image.

Coordinates are zero-based (row, column). Each arrow lists its circle
cell followed by its shaft cells, in order toward the arrowhead.
"""

from sudoku.puzzle import SudokuPuzzle

NAME = "Arrow Sudoku #001"


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [5, 2, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    # Top section
    puzzle.add_arrow([(0, 2)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(1, 2)], [(2, 3), (1, 3)])
    puzzle.add_arrow([(1, 4)], [(0, 4), (0, 5)])
    puzzle.add_arrow([(1, 5)], [(1, 6), (0, 6)])
    puzzle.add_arrow([(1, 7)], [(2, 6), (3, 5), (2, 4)])
    puzzle.add_arrow([(2, 5)], [(3, 6), (4, 6)])

    # Middle section
    puzzle.add_arrow([(3, 2)], [(3, 3), (2, 2), (2, 1)])
    puzzle.add_arrow([(3, 8)], [(4, 8), (4, 7)])
    puzzle.add_arrow([(4, 1)], [(5, 0), (4, 0)])
    puzzle.add_arrow([(5, 1)], [(4, 2), (4, 3)])
    puzzle.add_arrow([(5, 3)], [(6, 3), (7, 4)])
    puzzle.add_arrow([(5, 6)], [(5, 5), (6, 4)])

    # Bottom section
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (6, 8), (6, 7)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (8, 2)])
    puzzle.add_arrow([(7, 6)], [(7, 5), (8, 4)])

    return puzzle