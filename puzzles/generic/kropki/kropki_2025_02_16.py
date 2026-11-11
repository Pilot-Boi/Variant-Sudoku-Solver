"""PuzzleMadness Kropki Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/2/16'
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
        [6, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 0), (0, 1), 'black')
    puzzle.add_kropki_dot((0, 3), (0, 4), 'white')
    puzzle.add_kropki_dot((0, 6), (0, 7), 'white')
    puzzle.add_kropki_dot((1, 1), (1, 2), 'white')
    puzzle.add_kropki_dot((1, 4), (1, 5), 'white')
    puzzle.add_kropki_dot((1, 7), (1, 8), 'black')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 1), (2, 2), 'black')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'white')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'black')
    puzzle.add_kropki_dot((2, 5), (2, 6), 'white')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'black')
    puzzle.add_kropki_dot((3, 5), (3, 6), 'white')
    puzzle.add_kropki_dot((3, 6), (3, 7), 'white')
    puzzle.add_kropki_dot((4, 2), (4, 3), 'white')
    puzzle.add_kropki_dot((4, 4), (4, 5), 'white')
    puzzle.add_kropki_dot((5, 4), (5, 5), 'white')
    puzzle.add_kropki_dot((5, 6), (5, 7), 'white')
    puzzle.add_kropki_dot((6, 2), (6, 3), 'white')
    puzzle.add_kropki_dot((6, 4), (6, 5), 'white')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'black')
    puzzle.add_kropki_dot((8, 2), (8, 3), 'white')
    puzzle.add_kropki_dot((8, 4), (8, 5), 'white')
    puzzle.add_kropki_dot((0, 1), (1, 1), 'white')
    puzzle.add_kropki_dot((0, 4), (1, 4), 'black')
    puzzle.add_kropki_dot((2, 3), (3, 3), 'white')
    puzzle.add_kropki_dot((2, 6), (3, 6), 'black')
    puzzle.add_kropki_dot((2, 8), (3, 8), 'white')
    puzzle.add_kropki_dot((3, 1), (4, 1), 'white')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'white')
    puzzle.add_kropki_dot((3, 3), (4, 3), 'black')
    puzzle.add_kropki_dot((3, 5), (4, 5), 'black')
    puzzle.add_kropki_dot((4, 0), (5, 0), 'black')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'white')
    puzzle.add_kropki_dot((4, 8), (5, 8), 'black')
    puzzle.add_kropki_dot((5, 0), (6, 0), 'black')
    puzzle.add_kropki_dot((5, 3), (6, 3), 'white')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'black')
    puzzle.add_kropki_dot((5, 8), (6, 8), 'black')
    puzzle.add_kropki_dot((6, 4), (7, 4), 'white')
    puzzle.add_kropki_dot((6, 7), (7, 7), 'white')
    puzzle.add_kropki_dot((6, 8), (7, 8), 'white')
    puzzle.add_kropki_dot((7, 1), (8, 1), 'white')
    puzzle.add_kropki_dot((7, 3), (8, 3), 'white')
    puzzle.add_kropki_dot((7, 8), (8, 8), 'white')

    return puzzle
