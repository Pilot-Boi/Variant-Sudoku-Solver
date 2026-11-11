"""PuzzleMadness Kropki Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/1/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((1, 1), (1, 2), 'white')
    puzzle.add_kropki_dot((1, 5), (1, 6), 'white')
    puzzle.add_kropki_dot((1, 7), (1, 8), 'black')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'black')
    puzzle.add_kropki_dot((2, 1), (2, 2), 'white')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'black')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'black')
    puzzle.add_kropki_dot((4, 1), (4, 2), 'white')
    puzzle.add_kropki_dot((4, 2), (4, 3), 'white')
    puzzle.add_kropki_dot((4, 7), (4, 8), 'white')
    puzzle.add_kropki_dot((5, 0), (5, 1), 'black')
    puzzle.add_kropki_dot((5, 7), (5, 8), 'white')
    puzzle.add_kropki_dot((6, 0), (6, 1), 'white')
    puzzle.add_kropki_dot((6, 4), (6, 5), 'white')
    puzzle.add_kropki_dot((8, 2), (8, 3), 'white')
    puzzle.add_kropki_dot((8, 4), (8, 5), 'black')
    puzzle.add_kropki_dot((0, 2), (1, 2), 'white')
    puzzle.add_kropki_dot((0, 3), (1, 3), 'black')
    puzzle.add_kropki_dot((0, 4), (1, 4), 'black')
    puzzle.add_kropki_dot((0, 6), (1, 6), 'black')
    puzzle.add_kropki_dot((0, 8), (1, 8), 'black')
    puzzle.add_kropki_dot((1, 0), (2, 0), 'white')
    puzzle.add_kropki_dot((1, 6), (2, 6), 'white')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'white')
    puzzle.add_kropki_dot((2, 0), (3, 0), 'black')
    puzzle.add_kropki_dot((2, 2), (3, 2), 'black')
    puzzle.add_kropki_dot((2, 3), (3, 3), 'black')
    puzzle.add_kropki_dot((2, 5), (3, 5), 'white')
    puzzle.add_kropki_dot((3, 3), (4, 3), 'white')
    puzzle.add_kropki_dot((4, 0), (5, 0), 'black')
    puzzle.add_kropki_dot((4, 7), (5, 7), 'black')
    puzzle.add_kropki_dot((5, 5), (6, 5), 'white')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'white')
    puzzle.add_kropki_dot((5, 8), (6, 8), 'white')
    puzzle.add_kropki_dot((6, 2), (7, 2), 'white')
    puzzle.add_kropki_dot((6, 5), (7, 5), 'white')
    puzzle.add_kropki_dot((6, 7), (7, 7), 'black')
    puzzle.add_kropki_dot((7, 2), (8, 2), 'white')
    puzzle.add_kropki_dot((7, 7), (8, 7), 'white')

    return puzzle
