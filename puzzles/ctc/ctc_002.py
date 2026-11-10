"""
Wanddeko by Myxo

Imported from https://sudokupad.app/2004fp6a0r

Rules:
Normal sudoku rules apply. 
Digits separated by a white dot are consecutive. A black dot sits between two digits where one is double the other. Not all dots are necessarily given. 
Inequality signs between two cells point towards the smaller digit.
"""

from sudoku.puzzle import SudokuPuzzle

NAME = "Wanddeko — Myxo"
SOURCE_URL = "https://sudokupad.app/2004fp6a0r"

# Solution string provided by the source puzzle data.
SOLUTION = "417586923328914567596732148785641239264379851931258476842167395173495682659823714"


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)
    puzzle.add_kropki_dot((2, 1), (3, 1), "white")
    puzzle.add_kropki_dot((2, 3), (3, 3), "white")
    puzzle.add_kropki_dot((2, 5), (3, 5), "white")
    puzzle.add_kropki_dot((2, 7), (3, 7), "white")
    puzzle.add_kropki_dot((5, 0), (6, 0), "white")
    puzzle.add_kropki_dot((5, 3), (6, 3), "white")
    puzzle.add_kropki_dot((5, 5), (6, 5), "white")
    puzzle.add_kropki_dot((5, 6), (6, 6), "white")
    puzzle.add_kropki_dot((5, 8), (6, 8), "white")
    puzzle.add_kropki_dot((1, 2), (1, 3), "white")
    puzzle.add_kropki_dot((2, 5), (2, 6), "white")
    puzzle.add_kropki_dot((3, 2), (3, 3), "white")
    puzzle.add_kropki_dot((4, 5), (4, 6), "white")
    puzzle.add_kropki_dot((5, 2), (5, 3), "white")
    puzzle.add_kropki_dot((5, 5), (5, 6), "black")
    puzzle.add_kropki_dot((7, 2), (7, 3), "white")
    puzzle.add_inequality((2, 0), (3, 0), "<")
    puzzle.add_inequality((2, 4), (3, 4), "<")
    puzzle.add_inequality((2, 6), (3, 6), "<")
    puzzle.add_inequality((2, 8), (3, 8), "<")
    puzzle.add_inequality((5, 1), (6, 1), "<")
    puzzle.add_inequality((5, 4), (6, 4), "<")
    puzzle.add_inequality((5, 7), (6, 7), "<")
    puzzle.add_inequality((0, 3), (0, 2), "<")
    puzzle.add_inequality((0, 5), (0, 6), "<")
    puzzle.add_inequality((1, 5), (1, 6), "<")
    puzzle.add_inequality((4, 3), (4, 2), "<")
    puzzle.add_inequality((6, 3), (6, 2), "<")
    puzzle.add_inequality((7, 5), (7, 6), "<")
    puzzle.add_inequality((8, 3), (8, 2), "<")
    puzzle.add_inequality((8, 5), (8, 6), "<")

    return puzzle
