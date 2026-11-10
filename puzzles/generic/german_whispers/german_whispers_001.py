
    
  
from sudoku.puzzle import SudokuPuzzle

NAME = "German Whispers Sudoku #001"


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    # Upper-left closed loop. Split into an open path and its closing
    # edge because GermanWhispersConstraint rejects repeated cells.
    puzzle.add_german_whispers([
        (3, 1), (3, 0), (2, 0), (1, 0), (0, 0),
        (0, 1), (1, 2), (2, 2),
    ])
    puzzle.add_german_whispers([(2, 2), (3, 1)])

    # Upper-right zigzag, starting at R4C5.
    puzzle.add_german_whispers([
        (3, 4), (3, 5), (3, 6), (2, 7),
        (1, 6), (0, 7), (0, 8),
    ])

    # Lower-left W-shaped line with downward endpoints.
    puzzle.add_german_whispers([
        (8, 1), (7, 1), (6, 1), (5, 2),
        (6, 3), (5, 4), (6, 5), (7, 5), (8, 5),
    ])

    # Lower-right bent line.
    puzzle.add_german_whispers([
        (5, 7), (5, 8), (6, 8), (6, 7), (7, 7),
    ])

    return puzzle