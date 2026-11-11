"""PuzzleMadness Kropki Sudoku — 2025-03-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-03-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/3/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 0), (0, 1), 'black')
    puzzle.add_kropki_dot((0, 5), (0, 6), 'black')
    puzzle.add_kropki_dot((1, 1), (1, 2), 'white')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'white')
    puzzle.add_kropki_dot((2, 5), (2, 6), 'white')
    puzzle.add_kropki_dot((3, 0), (3, 1), 'white')
    puzzle.add_kropki_dot((3, 6), (3, 7), 'white')
    puzzle.add_kropki_dot((4, 1), (4, 2), 'white')
    puzzle.add_kropki_dot((4, 4), (4, 5), 'white')
    puzzle.add_kropki_dot((4, 7), (4, 8), 'white')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'black')
    puzzle.add_kropki_dot((5, 5), (5, 6), 'white')
    puzzle.add_kropki_dot((5, 6), (5, 7), 'black')
    puzzle.add_kropki_dot((6, 1), (6, 2), 'white')
    puzzle.add_kropki_dot((7, 3), (7, 4), 'black')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 2), (8, 3), 'white')
    puzzle.add_kropki_dot((8, 5), (8, 6), 'white')
    puzzle.add_kropki_dot((0, 0), (1, 0), 'white')
    puzzle.add_kropki_dot((0, 5), (1, 5), 'white')
    puzzle.add_kropki_dot((0, 6), (1, 6), 'white')
    puzzle.add_kropki_dot((0, 7), (1, 7), 'black')
    puzzle.add_kropki_dot((0, 8), (1, 8), 'white')
    puzzle.add_kropki_dot((1, 0), (2, 0), 'black')
    puzzle.add_kropki_dot((1, 2), (2, 2), 'white')
    puzzle.add_kropki_dot((1, 3), (2, 3), 'black')
    puzzle.add_kropki_dot((1, 4), (2, 4), 'white')
    puzzle.add_kropki_dot((1, 8), (2, 8), 'black')
    puzzle.add_kropki_dot((2, 4), (3, 4), 'white')
    puzzle.add_kropki_dot((2, 5), (3, 5), 'white')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'white')
    puzzle.add_kropki_dot((3, 6), (4, 6), 'black')
    puzzle.add_kropki_dot((4, 1), (5, 1), 'black')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'white')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'white')
    puzzle.add_kropki_dot((4, 5), (5, 5), 'white')
    puzzle.add_kropki_dot((4, 8), (5, 8), 'white')
    puzzle.add_kropki_dot((5, 2), (6, 2), 'white')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'white')
    puzzle.add_kropki_dot((6, 1), (7, 1), 'white')
    puzzle.add_kropki_dot((7, 1), (8, 1), 'black')
    puzzle.add_kropki_dot((7, 3), (8, 3), 'white')
    puzzle.add_kropki_dot((7, 4), (8, 4), 'white')
    puzzle.add_kropki_dot((7, 5), (8, 5), 'white')

    return puzzle
