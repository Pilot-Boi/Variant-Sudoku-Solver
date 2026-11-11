"""PuzzleMadness Kropki Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 5), (0, 6), 'black')
    puzzle.add_kropki_dot((1, 0), (1, 1), 'black')
    puzzle.add_kropki_dot((1, 1), (1, 2), 'white')
    puzzle.add_kropki_dot((1, 2), (1, 3), 'white')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'black')
    puzzle.add_kropki_dot((2, 6), (2, 7), 'black')
    puzzle.add_kropki_dot((3, 1), (3, 2), 'black')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'black')
    puzzle.add_kropki_dot((5, 2), (5, 3), 'white')
    puzzle.add_kropki_dot((5, 4), (5, 5), 'black')
    puzzle.add_kropki_dot((5, 7), (5, 8), 'white')
    puzzle.add_kropki_dot((6, 4), (6, 5), 'white')
    puzzle.add_kropki_dot((6, 6), (6, 7), 'white')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'black')
    puzzle.add_kropki_dot((7, 3), (7, 4), 'white')
    puzzle.add_kropki_dot((7, 5), (7, 6), 'black')
    puzzle.add_kropki_dot((8, 0), (8, 1), 'white')
    puzzle.add_kropki_dot((8, 5), (8, 6), 'white')
    puzzle.add_kropki_dot((8, 7), (8, 8), 'black')
    puzzle.add_kropki_dot((0, 3), (1, 3), 'black')
    puzzle.add_kropki_dot((0, 4), (1, 4), 'white')
    puzzle.add_kropki_dot((0, 5), (1, 5), 'black')
    puzzle.add_kropki_dot((1, 1), (2, 1), 'white')
    puzzle.add_kropki_dot((1, 5), (2, 5), 'white')
    puzzle.add_kropki_dot((2, 7), (3, 7), 'white')
    puzzle.add_kropki_dot((2, 8), (3, 8), 'white')
    puzzle.add_kropki_dot((3, 0), (4, 0), 'black')
    puzzle.add_kropki_dot((3, 4), (4, 4), 'white')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'black')
    puzzle.add_kropki_dot((4, 7), (5, 7), 'black')
    puzzle.add_kropki_dot((5, 2), (6, 2), 'white')
    puzzle.add_kropki_dot((5, 4), (6, 4), 'white')
    puzzle.add_kropki_dot((5, 5), (6, 5), 'white')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'white')
    puzzle.add_kropki_dot((5, 8), (6, 8), 'white')
    puzzle.add_kropki_dot((6, 7), (7, 7), 'white')
    puzzle.add_kropki_dot((7, 5), (8, 5), 'white')
    puzzle.add_kropki_dot((7, 6), (8, 6), 'black')
    puzzle.add_kropki_dot((7, 8), (8, 8), 'white')

    return puzzle
