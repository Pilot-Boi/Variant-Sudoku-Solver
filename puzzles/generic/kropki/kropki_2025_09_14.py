"""PuzzleMadness Kropki Sudoku — 2025-09-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-09-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/9/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 0), (0, 1), 'white')
    puzzle.add_kropki_dot((0, 7), (0, 8), 'black')
    puzzle.add_kropki_dot((1, 0), (1, 1), 'white')
    puzzle.add_kropki_dot((1, 6), (1, 7), 'white')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'white')
    puzzle.add_kropki_dot((2, 5), (2, 6), 'black')
    puzzle.add_kropki_dot((3, 2), (3, 3), 'white')
    puzzle.add_kropki_dot((3, 5), (3, 6), 'white')
    puzzle.add_kropki_dot((4, 0), (4, 1), 'white')
    puzzle.add_kropki_dot((5, 0), (5, 1), 'white')
    puzzle.add_kropki_dot((5, 1), (5, 2), 'black')
    puzzle.add_kropki_dot((5, 2), (5, 3), 'white')
    puzzle.add_kropki_dot((6, 0), (6, 1), 'white')
    puzzle.add_kropki_dot((6, 4), (6, 5), 'black')
    puzzle.add_kropki_dot((7, 3), (7, 4), 'white')
    puzzle.add_kropki_dot((7, 4), (7, 5), 'black')
    puzzle.add_kropki_dot((7, 5), (7, 6), 'white')
    puzzle.add_kropki_dot((7, 6), (7, 7), 'black')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'black')
    puzzle.add_kropki_dot((8, 1), (8, 2), 'black')
    puzzle.add_kropki_dot((0, 2), (1, 2), 'white')
    puzzle.add_kropki_dot((0, 3), (1, 3), 'white')
    puzzle.add_kropki_dot((1, 0), (2, 0), 'white')
    puzzle.add_kropki_dot((1, 1), (2, 1), 'black')
    puzzle.add_kropki_dot((1, 3), (2, 3), 'black')
    puzzle.add_kropki_dot((1, 5), (2, 5), 'white')
    puzzle.add_kropki_dot((2, 4), (3, 4), 'white')
    puzzle.add_kropki_dot((2, 5), (3, 5), 'white')
    puzzle.add_kropki_dot((2, 7), (3, 7), 'white')
    puzzle.add_kropki_dot((3, 1), (4, 1), 'white')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'black')
    puzzle.add_kropki_dot((3, 3), (4, 3), 'white')
    puzzle.add_kropki_dot((3, 7), (4, 7), 'black')
    puzzle.add_kropki_dot((4, 2), (5, 2), 'white')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'white')
    puzzle.add_kropki_dot((5, 1), (6, 1), 'black')
    puzzle.add_kropki_dot((5, 4), (6, 4), 'black')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'white')
    puzzle.add_kropki_dot((7, 1), (8, 1), 'white')
    puzzle.add_kropki_dot((7, 4), (8, 4), 'white')
    puzzle.add_kropki_dot((7, 5), (8, 5), 'white')

    return puzzle
