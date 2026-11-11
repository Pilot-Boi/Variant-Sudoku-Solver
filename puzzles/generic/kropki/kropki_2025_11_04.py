"""PuzzleMadness Kropki Sudoku — 2025-11-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-11-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/11/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 3), (0, 4), 'white')
    puzzle.add_kropki_dot((0, 6), (0, 7), 'black')
    puzzle.add_kropki_dot((1, 1), (1, 2), 'white')
    puzzle.add_kropki_dot((1, 4), (1, 5), 'white')
    puzzle.add_kropki_dot((1, 5), (1, 6), 'white')
    puzzle.add_kropki_dot((2, 1), (2, 2), 'white')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'white')
    puzzle.add_kropki_dot((3, 2), (3, 3), 'black')
    puzzle.add_kropki_dot((3, 6), (3, 7), 'black')
    puzzle.add_kropki_dot((3, 7), (3, 8), 'white')
    puzzle.add_kropki_dot((4, 2), (4, 3), 'black')
    puzzle.add_kropki_dot((4, 5), (4, 6), 'white')
    puzzle.add_kropki_dot((4, 6), (4, 7), 'black')
    puzzle.add_kropki_dot((4, 7), (4, 8), 'white')
    puzzle.add_kropki_dot((5, 2), (5, 3), 'black')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'white')
    puzzle.add_kropki_dot((5, 5), (5, 6), 'white')
    puzzle.add_kropki_dot((6, 1), (6, 2), 'white')
    puzzle.add_kropki_dot((6, 3), (6, 4), 'black')
    puzzle.add_kropki_dot((6, 4), (6, 5), 'white')
    puzzle.add_kropki_dot((7, 6), (7, 7), 'black')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 0), (8, 1), 'black')
    puzzle.add_kropki_dot((8, 1), (8, 2), 'white')
    puzzle.add_kropki_dot((8, 5), (8, 6), 'white')
    puzzle.add_kropki_dot((8, 6), (8, 7), 'white')
    puzzle.add_kropki_dot((0, 0), (1, 0), 'black')
    puzzle.add_kropki_dot((0, 8), (1, 8), 'black')
    puzzle.add_kropki_dot((1, 1), (2, 1), 'black')
    puzzle.add_kropki_dot((1, 5), (2, 5), 'black')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'white')
    puzzle.add_kropki_dot((1, 8), (2, 8), 'white')
    puzzle.add_kropki_dot((2, 2), (3, 2), 'black')
    puzzle.add_kropki_dot((3, 5), (4, 5), 'white')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'white')
    puzzle.add_kropki_dot((4, 8), (5, 8), 'black')
    puzzle.add_kropki_dot((5, 0), (6, 0), 'white')
    puzzle.add_kropki_dot((5, 1), (6, 1), 'black')
    puzzle.add_kropki_dot((5, 3), (6, 3), 'white')
    puzzle.add_kropki_dot((5, 4), (6, 4), 'black')
    puzzle.add_kropki_dot((6, 0), (7, 0), 'white')
    puzzle.add_kropki_dot((6, 1), (7, 1), 'white')
    puzzle.add_kropki_dot((6, 6), (7, 6), 'black')
    puzzle.add_kropki_dot((7, 0), (8, 0), 'white')
    puzzle.add_kropki_dot((7, 8), (8, 8), 'black')

    return puzzle
