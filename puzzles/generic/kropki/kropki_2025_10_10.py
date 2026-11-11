"""PuzzleMadness Kropki Sudoku — 2025-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/10/10'
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 1), (0, 2), 'white')
    puzzle.add_kropki_dot((0, 2), (0, 3), 'white')
    puzzle.add_kropki_dot((0, 4), (0, 5), 'white')
    puzzle.add_kropki_dot((0, 5), (0, 6), 'white')
    puzzle.add_kropki_dot((1, 1), (1, 2), 'black')
    puzzle.add_kropki_dot((1, 7), (1, 8), 'black')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'white')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'white')
    puzzle.add_kropki_dot((2, 6), (2, 7), 'white')
    puzzle.add_kropki_dot((3, 1), (3, 2), 'white')
    puzzle.add_kropki_dot((3, 2), (3, 3), 'black')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'black')
    puzzle.add_kropki_dot((3, 4), (3, 5), 'black')
    puzzle.add_kropki_dot((3, 6), (3, 7), 'black')
    puzzle.add_kropki_dot((3, 7), (3, 8), 'white')
    puzzle.add_kropki_dot((4, 0), (4, 1), 'white')
    puzzle.add_kropki_dot((4, 5), (4, 6), 'black')
    puzzle.add_kropki_dot((4, 6), (4, 7), 'black')
    puzzle.add_kropki_dot((5, 0), (5, 1), 'white')
    puzzle.add_kropki_dot((5, 1), (5, 2), 'black')
    puzzle.add_kropki_dot((5, 7), (5, 8), 'white')
    puzzle.add_kropki_dot((6, 1), (6, 2), 'black')
    puzzle.add_kropki_dot((6, 2), (6, 3), 'white')
    puzzle.add_kropki_dot((6, 6), (6, 7), 'white')
    puzzle.add_kropki_dot((6, 7), (6, 8), 'white')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'white')
    puzzle.add_kropki_dot((7, 3), (7, 4), 'white')
    puzzle.add_kropki_dot((7, 4), (7, 5), 'black')
    puzzle.add_kropki_dot((7, 5), (7, 6), 'white')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 4), (8, 5), 'white')
    puzzle.add_kropki_dot((0, 4), (1, 4), 'white')
    puzzle.add_kropki_dot((1, 0), (2, 0), 'black')
    puzzle.add_kropki_dot((1, 6), (2, 6), 'white')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'white')
    puzzle.add_kropki_dot((2, 2), (3, 2), 'white')
    puzzle.add_kropki_dot((2, 3), (3, 3), 'black')
    puzzle.add_kropki_dot((2, 5), (3, 5), 'black')
    puzzle.add_kropki_dot((2, 6), (3, 6), 'black')
    puzzle.add_kropki_dot((2, 7), (3, 7), 'white')
    puzzle.add_kropki_dot((3, 0), (4, 0), 'white')
    puzzle.add_kropki_dot((3, 4), (4, 4), 'white')
    puzzle.add_kropki_dot((3, 6), (4, 6), 'white')
    puzzle.add_kropki_dot((4, 0), (5, 0), 'black')
    puzzle.add_kropki_dot((4, 1), (5, 1), 'white')
    puzzle.add_kropki_dot((4, 2), (5, 2), 'black')
    puzzle.add_kropki_dot((5, 1), (6, 1), 'black')
    puzzle.add_kropki_dot((5, 2), (6, 2), 'black')
    puzzle.add_kropki_dot((5, 5), (6, 5), 'white')
    puzzle.add_kropki_dot((5, 7), (6, 7), 'white')
    puzzle.add_kropki_dot((5, 8), (6, 8), 'white')
    puzzle.add_kropki_dot((6, 5), (7, 5), 'white')
    puzzle.add_kropki_dot((7, 2), (8, 2), 'white')
    puzzle.add_kropki_dot((7, 8), (8, 8), 'black')

    return puzzle
