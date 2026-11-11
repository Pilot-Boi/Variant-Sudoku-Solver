"""PuzzleMadness Kropki Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 4), (0, 5), 'black')
    puzzle.add_kropki_dot((1, 1), (1, 2), 'black')
    puzzle.add_kropki_dot((1, 4), (1, 5), 'white')
    puzzle.add_kropki_dot((1, 5), (1, 6), 'black')
    puzzle.add_kropki_dot((1, 6), (1, 7), 'white')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'black')
    puzzle.add_kropki_dot((2, 6), (2, 7), 'white')
    puzzle.add_kropki_dot((3, 2), (3, 3), 'white')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'black')
    puzzle.add_kropki_dot((3, 7), (3, 8), 'white')
    puzzle.add_kropki_dot((4, 0), (4, 1), 'black')
    puzzle.add_kropki_dot((4, 2), (4, 3), 'black')
    puzzle.add_kropki_dot((4, 6), (4, 7), 'white')
    puzzle.add_kropki_dot((4, 7), (4, 8), 'black')
    puzzle.add_kropki_dot((5, 0), (5, 1), 'white')
    puzzle.add_kropki_dot((5, 1), (5, 2), 'black')
    puzzle.add_kropki_dot((6, 0), (6, 1), 'white')
    puzzle.add_kropki_dot((6, 1), (6, 2), 'white')
    puzzle.add_kropki_dot((6, 7), (6, 8), 'white')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'white')
    puzzle.add_kropki_dot((7, 4), (7, 5), 'black')
    puzzle.add_kropki_dot((7, 5), (7, 6), 'white')
    puzzle.add_kropki_dot((8, 4), (8, 5), 'black')
    puzzle.add_kropki_dot((8, 7), (8, 8), 'black')
    puzzle.add_kropki_dot((0, 1), (1, 1), 'white')
    puzzle.add_kropki_dot((1, 1), (2, 1), 'white')
    puzzle.add_kropki_dot((1, 2), (2, 2), 'white')
    puzzle.add_kropki_dot((1, 6), (2, 6), 'black')
    puzzle.add_kropki_dot((2, 0), (3, 0), 'white')
    puzzle.add_kropki_dot((2, 2), (3, 2), 'white')
    puzzle.add_kropki_dot((2, 5), (3, 5), 'white')
    puzzle.add_kropki_dot((2, 6), (3, 6), 'white')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'white')
    puzzle.add_kropki_dot((3, 3), (4, 3), 'white')
    puzzle.add_kropki_dot((3, 4), (4, 4), 'white')
    puzzle.add_kropki_dot((3, 7), (4, 7), 'white')
    puzzle.add_kropki_dot((4, 1), (5, 1), 'black')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'white')
    puzzle.add_kropki_dot((5, 0), (6, 0), 'white')
    puzzle.add_kropki_dot((5, 1), (6, 1), 'white')
    puzzle.add_kropki_dot((5, 8), (6, 8), 'white')
    puzzle.add_kropki_dot((6, 4), (7, 4), 'black')
    puzzle.add_kropki_dot((6, 7), (7, 7), 'white')
    puzzle.add_kropki_dot((7, 0), (8, 0), 'white')
    puzzle.add_kropki_dot((7, 5), (8, 5), 'white')

    return puzzle
