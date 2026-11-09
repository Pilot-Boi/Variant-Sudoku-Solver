""" 
    Center Focus by DedaKosta
    
    - Normal sudoku rules apply - Place digits 1-9 once each in every row, column and 3x3 box
    - Digits separated by a white dot are consecutive, digits separated by a black dot are in a 1:2 ratio, i.e. one digit is double the other. Not all dots are given
    - Adjacent digits on a green line must have a difference of at least 5
    - Digits on an arrow sum to the digit in that arrow's circle
    - Digits must increase along a thermometer starting from the bulb
    - Digits cannot repeat on both marked diagonals
"""

from sudoku.puzzle import SudokuPuzzle

NAME = "Center Focus — DedaKosta"


def create_puzzle():
    puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

    # Both long diagonals contain digits 1–9 without repetition.
    puzzle.add_diagonal_constraints()

    # Green German Whispers lines (adjacent digits differ by at least 5).
    puzzle.add_german_whispers([
        (0, 5), (1, 5), (1, 6), (2, 6),
        (2, 7), (3, 7), (3, 8),
    ])
    puzzle.add_german_whispers([
        (5, 0), (5, 1), (6, 1), (6, 2),
        (7, 2), (7, 3), (8, 3),
    ])

    # Thermometers, bulb first, tip last.
    puzzle.add_thermometer([
        (4, 1), (4, 2), (4, 3), (5, 3), (6, 3),
    ])
    puzzle.add_thermometer([
        (4, 7), (4, 6), (4, 5), (3, 5), (2, 5),
    ])

    # Kropki dots: explicit dots only (no negative Kropki rule).
    # White: consecutive digits.
    puzzle.add_kropki_dot((1, 1), (1, 2), "white")  # R2C2–R2C3
    puzzle.add_kropki_dot((1, 2), (2, 2), "white")  # R2C3–R3C3
    puzzle.add_kropki_dot((4, 4), (4, 5), "white")  # R5C5–R5C6

    # Black: one digit is twice the other.
    puzzle.add_kropki_dot((2, 3), (2, 4), "black")  # R3C4–R3C5
    puzzle.add_kropki_dot((4, 5), (4, 6), "black")  # R5C6–R5C7
    puzzle.add_kropki_dot((6, 4), (7, 4), "black")  # R7C5–R8C5

    # Arrows: sum of shaft digits equals the circle digit.
    # Circle R4C5; shaft travels left to R4C4, then up to R3C4.
    puzzle.add_arrow([(3, 4)], [(3, 3), (2, 3)])

    # Circle R6C5; shaft travels right to R6C6, then down to R7C6.
    puzzle.add_arrow([(5, 4)], [(5, 5), (6, 5)])

    return puzzle