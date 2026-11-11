"""PuzzleMadness Kropki Sudoku — 2025-11-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-11-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/11/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 0), (0, 1), 'white')
    puzzle.add_kropki_dot((0, 2), (0, 3), 'white')
    puzzle.add_kropki_dot((0, 5), (0, 6), 'white')
    puzzle.add_kropki_dot((1, 0), (1, 1), 'black')
    puzzle.add_kropki_dot((2, 4), (2, 5), 'white')
    puzzle.add_kropki_dot((2, 5), (2, 6), 'black')
    puzzle.add_kropki_dot((3, 0), (3, 1), 'white')
    puzzle.add_kropki_dot((3, 5), (3, 6), 'white')
    puzzle.add_kropki_dot((3, 7), (3, 8), 'white')
    puzzle.add_kropki_dot((5, 2), (5, 3), 'white')
    puzzle.add_kropki_dot((5, 7), (5, 8), 'white')
    puzzle.add_kropki_dot((6, 5), (6, 6), 'white')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'black')
    puzzle.add_kropki_dot((7, 2), (7, 3), 'white')
    puzzle.add_kropki_dot((0, 0), (1, 0), 'white')
    puzzle.add_kropki_dot((0, 6), (1, 6), 'white')
    puzzle.add_kropki_dot((1, 4), (2, 4), 'black')
    puzzle.add_kropki_dot((2, 0), (3, 0), 'white')
    puzzle.add_kropki_dot((2, 5), (3, 5), 'black')
    puzzle.add_kropki_dot((3, 1), (4, 1), 'white')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'black')
    puzzle.add_kropki_dot((3, 7), (4, 7), 'black')
    puzzle.add_kropki_dot((4, 0), (5, 0), 'black')
    puzzle.add_kropki_dot((4, 5), (5, 5), 'white')
    puzzle.add_kropki_dot((5, 3), (6, 3), 'white')
    puzzle.add_kropki_dot((5, 4), (6, 4), 'white')
    puzzle.add_kropki_dot((5, 7), (6, 7), 'white')
    puzzle.add_kropki_dot((6, 0), (7, 0), 'white')
    puzzle.add_kropki_dot((6, 1), (7, 1), 'white')
    puzzle.add_kropki_dot((6, 5), (7, 5), 'white')
    puzzle.add_kropki_dot((6, 6), (7, 6), 'white')
    puzzle.add_kropki_dot((7, 4), (8, 4), 'black')
    puzzle.add_kropki_dot((7, 6), (8, 6), 'white')

    return puzzle
