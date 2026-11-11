"""PuzzleMadness Kropki Sudoku — 2025-11-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-11-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/11/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((1, 2), (1, 3), 'white')
    puzzle.add_kropki_dot((1, 4), (1, 5), 'white')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'white')
    puzzle.add_kropki_dot((2, 5), (2, 6), 'white')
    puzzle.add_kropki_dot((2, 7), (2, 8), 'black')
    puzzle.add_kropki_dot((3, 2), (3, 3), 'black')
    puzzle.add_kropki_dot((3, 6), (3, 7), 'black')
    puzzle.add_kropki_dot((4, 0), (4, 1), 'black')
    puzzle.add_kropki_dot((4, 3), (4, 4), 'white')
    puzzle.add_kropki_dot((4, 5), (4, 6), 'white')
    puzzle.add_kropki_dot((5, 0), (5, 1), 'black')
    puzzle.add_kropki_dot((5, 1), (5, 2), 'white')
    puzzle.add_kropki_dot((5, 6), (5, 7), 'black')
    puzzle.add_kropki_dot((6, 0), (6, 1), 'white')
    puzzle.add_kropki_dot((6, 3), (6, 4), 'black')
    puzzle.add_kropki_dot((6, 7), (6, 8), 'white')
    puzzle.add_kropki_dot((7, 2), (7, 3), 'white')
    puzzle.add_kropki_dot((7, 3), (7, 4), 'white')
    puzzle.add_kropki_dot((7, 4), (7, 5), 'black')
    puzzle.add_kropki_dot((7, 5), (7, 6), 'white')
    puzzle.add_kropki_dot((7, 6), (7, 7), 'black')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 3), (8, 4), 'white')
    puzzle.add_kropki_dot((0, 0), (1, 0), 'white')
    puzzle.add_kropki_dot((0, 2), (1, 2), 'black')
    puzzle.add_kropki_dot((0, 5), (1, 5), 'black')
    puzzle.add_kropki_dot((0, 6), (1, 6), 'white')
    puzzle.add_kropki_dot((1, 2), (2, 2), 'black')
    puzzle.add_kropki_dot((1, 6), (2, 6), 'white')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'black')
    puzzle.add_kropki_dot((1, 8), (2, 8), 'black')
    puzzle.add_kropki_dot((2, 4), (3, 4), 'white')
    puzzle.add_kropki_dot((2, 8), (3, 8), 'black')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'black')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'white')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'white')
    puzzle.add_kropki_dot((4, 5), (5, 5), 'white')
    puzzle.add_kropki_dot((4, 7), (5, 7), 'white')
    puzzle.add_kropki_dot((5, 0), (6, 0), 'black')
    puzzle.add_kropki_dot((5, 4), (6, 4), 'black')
    puzzle.add_kropki_dot((5, 7), (6, 7), 'white')
    puzzle.add_kropki_dot((6, 3), (7, 3), 'white')
    puzzle.add_kropki_dot((6, 6), (7, 6), 'white')
    puzzle.add_kropki_dot((6, 8), (7, 8), 'white')
    puzzle.add_kropki_dot((7, 2), (8, 2), 'white')
    puzzle.add_kropki_dot((7, 7), (8, 7), 'white')

    return puzzle
