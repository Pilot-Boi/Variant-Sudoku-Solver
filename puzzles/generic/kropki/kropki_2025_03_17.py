"""PuzzleMadness Kropki Sudoku — 2025-03-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-03-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/3/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 1), (0, 2), 'black')
    puzzle.add_kropki_dot((0, 5), (0, 6), 'black')
    puzzle.add_kropki_dot((0, 6), (0, 7), 'black')
    puzzle.add_kropki_dot((0, 7), (0, 8), 'black')
    puzzle.add_kropki_dot((2, 4), (2, 5), 'white')
    puzzle.add_kropki_dot((2, 7), (2, 8), 'white')
    puzzle.add_kropki_dot((3, 1), (3, 2), 'black')
    puzzle.add_kropki_dot((3, 2), (3, 3), 'white')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'black')
    puzzle.add_kropki_dot((4, 4), (4, 5), 'black')
    puzzle.add_kropki_dot((4, 7), (4, 8), 'white')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'black')
    puzzle.add_kropki_dot((5, 4), (5, 5), 'white')
    puzzle.add_kropki_dot((5, 5), (5, 6), 'white')
    puzzle.add_kropki_dot((6, 1), (6, 2), 'white')
    puzzle.add_kropki_dot((6, 3), (6, 4), 'black')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'black')
    puzzle.add_kropki_dot((7, 2), (7, 3), 'white')
    puzzle.add_kropki_dot((7, 4), (7, 5), 'white')
    puzzle.add_kropki_dot((7, 5), (7, 6), 'white')
    puzzle.add_kropki_dot((7, 6), (7, 7), 'white')
    puzzle.add_kropki_dot((0, 0), (1, 0), 'white')
    puzzle.add_kropki_dot((0, 6), (1, 6), 'white')
    puzzle.add_kropki_dot((0, 7), (1, 7), 'white')
    puzzle.add_kropki_dot((0, 8), (1, 8), 'white')
    puzzle.add_kropki_dot((1, 0), (2, 0), 'black')
    puzzle.add_kropki_dot((1, 3), (2, 3), 'white')
    puzzle.add_kropki_dot((1, 4), (2, 4), 'white')
    puzzle.add_kropki_dot((1, 5), (2, 5), 'black')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'white')
    puzzle.add_kropki_dot((2, 4), (3, 4), 'black')
    puzzle.add_kropki_dot((2, 7), (3, 7), 'white')
    puzzle.add_kropki_dot((3, 1), (4, 1), 'white')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'white')
    puzzle.add_kropki_dot((4, 0), (5, 0), 'white')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'white')
    puzzle.add_kropki_dot((4, 8), (5, 8), 'black')
    puzzle.add_kropki_dot((5, 3), (6, 3), 'black')
    puzzle.add_kropki_dot((5, 4), (6, 4), 'black')
    puzzle.add_kropki_dot((6, 5), (7, 5), 'black')
    puzzle.add_kropki_dot((7, 1), (8, 1), 'white')
    puzzle.add_kropki_dot((7, 3), (8, 3), 'black')
    puzzle.add_kropki_dot((7, 5), (8, 5), 'white')
    puzzle.add_kropki_dot((7, 8), (8, 8), 'black')

    return puzzle
