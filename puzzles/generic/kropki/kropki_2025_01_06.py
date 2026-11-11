"""PuzzleMadness Kropki Sudoku — 2025-01-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-01-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/1/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 0), (0, 1), 'white')
    puzzle.add_kropki_dot((0, 3), (0, 4), 'white')
    puzzle.add_kropki_dot((1, 0), (1, 1), 'white')
    puzzle.add_kropki_dot((1, 6), (1, 7), 'black')
    puzzle.add_kropki_dot((1, 7), (1, 8), 'white')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'white')
    puzzle.add_kropki_dot((2, 4), (2, 5), 'black')
    puzzle.add_kropki_dot((2, 7), (2, 8), 'black')
    puzzle.add_kropki_dot((3, 5), (3, 6), 'white')
    puzzle.add_kropki_dot((3, 6), (3, 7), 'black')
    puzzle.add_kropki_dot((4, 2), (4, 3), 'white')
    puzzle.add_kropki_dot((4, 3), (4, 4), 'black')
    puzzle.add_kropki_dot((4, 7), (4, 8), 'black')
    puzzle.add_kropki_dot((5, 0), (5, 1), 'black')
    puzzle.add_kropki_dot((5, 2), (5, 3), 'white')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'black')
    puzzle.add_kropki_dot((5, 4), (5, 5), 'black')
    puzzle.add_kropki_dot((6, 2), (6, 3), 'white')
    puzzle.add_kropki_dot((7, 0), (7, 1), 'black')
    puzzle.add_kropki_dot((8, 1), (8, 2), 'white')
    puzzle.add_kropki_dot((8, 2), (8, 3), 'black')
    puzzle.add_kropki_dot((0, 2), (1, 2), 'white')
    puzzle.add_kropki_dot((1, 1), (2, 1), 'white')
    puzzle.add_kropki_dot((1, 4), (2, 4), 'black')
    puzzle.add_kropki_dot((1, 5), (2, 5), 'white')
    puzzle.add_kropki_dot((2, 2), (3, 2), 'black')
    puzzle.add_kropki_dot((2, 7), (3, 7), 'black')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'white')
    puzzle.add_kropki_dot((3, 6), (4, 6), 'white')
    puzzle.add_kropki_dot((3, 7), (4, 7), 'white')
    puzzle.add_kropki_dot((3, 8), (4, 8), 'black')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'white')
    puzzle.add_kropki_dot((5, 0), (6, 0), 'white')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'white')
    puzzle.add_kropki_dot((6, 3), (7, 3), 'black')
    puzzle.add_kropki_dot((6, 5), (7, 5), 'white')
    puzzle.add_kropki_dot((6, 6), (7, 6), 'white')
    puzzle.add_kropki_dot((6, 8), (7, 8), 'white')
    puzzle.add_kropki_dot((7, 3), (8, 3), 'white')
    puzzle.add_kropki_dot((7, 4), (8, 4), 'white')

    return puzzle
