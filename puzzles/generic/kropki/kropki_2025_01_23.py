"""PuzzleMadness Kropki Sudoku — 2025-01-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-01-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/1/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 0), (0, 1), 'white')
    puzzle.add_kropki_dot((0, 6), (0, 7), 'white')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'black')
    puzzle.add_kropki_dot((2, 6), (2, 7), 'black')
    puzzle.add_kropki_dot((2, 7), (2, 8), 'white')
    puzzle.add_kropki_dot((3, 0), (3, 1), 'black')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'black')
    puzzle.add_kropki_dot((3, 4), (3, 5), 'white')
    puzzle.add_kropki_dot((4, 0), (4, 1), 'white')
    puzzle.add_kropki_dot((4, 1), (4, 2), 'black')
    puzzle.add_kropki_dot((4, 4), (4, 5), 'white')
    puzzle.add_kropki_dot((5, 1), (5, 2), 'white')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'white')
    puzzle.add_kropki_dot((5, 4), (5, 5), 'black')
    puzzle.add_kropki_dot((5, 6), (5, 7), 'black')
    puzzle.add_kropki_dot((6, 1), (6, 2), 'white')
    puzzle.add_kropki_dot((6, 2), (6, 3), 'black')
    puzzle.add_kropki_dot((6, 3), (6, 4), 'white')
    puzzle.add_kropki_dot((7, 2), (7, 3), 'white')
    puzzle.add_kropki_dot((7, 3), (7, 4), 'black')
    puzzle.add_kropki_dot((7, 5), (7, 6), 'white')
    puzzle.add_kropki_dot((8, 5), (8, 6), 'white')
    puzzle.add_kropki_dot((0, 5), (1, 5), 'black')
    puzzle.add_kropki_dot((1, 1), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 0), (3, 0), 'black')
    puzzle.add_kropki_dot((2, 3), (3, 3), 'white')
    puzzle.add_kropki_dot((2, 5), (3, 5), 'white')
    puzzle.add_kropki_dot((2, 7), (3, 7), 'white')
    puzzle.add_kropki_dot((3, 8), (4, 8), 'black')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'black')
    puzzle.add_kropki_dot((5, 2), (6, 2), 'black')
    puzzle.add_kropki_dot((5, 5), (6, 5), 'white')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'white')
    puzzle.add_kropki_dot((5, 7), (6, 7), 'white')
    puzzle.add_kropki_dot((6, 7), (7, 7), 'black')
    puzzle.add_kropki_dot((7, 0), (8, 0), 'white')
    puzzle.add_kropki_dot((7, 1), (8, 1), 'white')
    puzzle.add_kropki_dot((7, 2), (8, 2), 'white')
    puzzle.add_kropki_dot((7, 5), (8, 5), 'white')
    puzzle.add_kropki_dot((7, 6), (8, 6), 'white')

    return puzzle
