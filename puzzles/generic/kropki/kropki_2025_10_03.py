"""PuzzleMadness Kropki Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 4), (0, 5), 'white')
    puzzle.add_kropki_dot((0, 6), (0, 7), 'white')
    puzzle.add_kropki_dot((1, 0), (1, 1), 'white')
    puzzle.add_kropki_dot((1, 1), (1, 2), 'black')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'white')
    puzzle.add_kropki_dot((2, 7), (2, 8), 'black')
    puzzle.add_kropki_dot((3, 0), (3, 1), 'white')
    puzzle.add_kropki_dot((4, 5), (4, 6), 'white')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'black')
    puzzle.add_kropki_dot((5, 4), (5, 5), 'white')
    puzzle.add_kropki_dot((5, 5), (5, 6), 'white')
    puzzle.add_kropki_dot((6, 4), (6, 5), 'black')
    puzzle.add_kropki_dot((6, 6), (6, 7), 'black')
    puzzle.add_kropki_dot((7, 0), (7, 1), 'black')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'white')
    puzzle.add_kropki_dot((7, 2), (7, 3), 'black')
    puzzle.add_kropki_dot((7, 6), (7, 7), 'white')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 7), (8, 8), 'black')
    puzzle.add_kropki_dot((0, 1), (1, 1), 'white')
    puzzle.add_kropki_dot((0, 4), (1, 4), 'white')
    puzzle.add_kropki_dot((0, 8), (1, 8), 'white')
    puzzle.add_kropki_dot((1, 4), (2, 4), 'white')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'white')
    puzzle.add_kropki_dot((1, 8), (2, 8), 'white')
    puzzle.add_kropki_dot((2, 1), (3, 1), 'black')
    puzzle.add_kropki_dot((2, 8), (3, 8), 'black')
    puzzle.add_kropki_dot((3, 8), (4, 8), 'white')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'white')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'black')
    puzzle.add_kropki_dot((4, 5), (5, 5), 'black')
    puzzle.add_kropki_dot((5, 4), (6, 4), 'black')
    puzzle.add_kropki_dot((5, 5), (6, 5), 'white')
    puzzle.add_kropki_dot((6, 5), (7, 5), 'white')
    puzzle.add_kropki_dot((6, 6), (7, 6), 'white')

    return puzzle
