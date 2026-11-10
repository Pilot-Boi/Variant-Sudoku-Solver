
    
  
"""Kropki Sudoku #001, transcribed from the supplied puzzle image.

Coordinates are zero-based (row, column). The image does not specify
negative Kropki rules, so undotted pairs are unrestricted by Kropki.
"""

from sudoku.puzzle import SudokuPuzzle

NAME = "Kropki Sudoku #001"


def create_puzzle():
    grid = [
        [4, 1, 0, 9, 0, 0, 7, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 6, 4],
        [0, 0, 0, 0, 0, 7, 0, 0, 1],
        [0, 9, 0, 7, 0, 0, 0, 8, 3],
        [0, 0, 0, 8, 0, 4, 0, 0, 0],
        [5, 8, 0, 0, 0, 6, 0, 2, 0],
        [1, 0, 0, 6, 0, 0, 0, 0, 0],
        [2, 6, 0, 4, 0, 0, 0, 1, 0],
        [0, 0, 8, 0, 0, 3, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    # White dots: adjacent digits differ by exactly 1.
    white_dots = [
        ((0, 4), (0, 5)),  # R1C5 - R1C6
        ((1, 0), (2, 0)),  # R2C1 - R3C1
        ((1, 5), (2, 5)),  # R2C6 - R3C6
        ((4, 0), (4, 1)),  # R5C1 - R5C2
        ((4, 4), (4, 5)),  # R5C5 - R5C6
        ((6, 1), (6, 2)),  # R7C2 - R7C3
    ]

    # Black dots: one adjacent digit is twice the other.
    black_dots = [
        ((2, 1), (2, 2)),  # R3C2 - R3C3
        ((5, 6), (5, 7)),  # R6C7 - R6C8
        ((7, 1), (7, 2)),  # R8C2 - R8C3
        ((8, 7), (8, 8)),  # R9C8 - R9C9
    ]

    for a, b in white_dots:
        puzzle.add_kropki_dot(a, b, "white")

    for a, b in black_dots:
        puzzle.add_kropki_dot(a, b, "black")

    return puzzle