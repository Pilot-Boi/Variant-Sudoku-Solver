"""PuzzleMadness Kropki Sudoku — 2025-06-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-06-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/6/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((1, 5), (1, 6), 'white')
    puzzle.add_kropki_dot((1, 7), (1, 8), 'black')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'white')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'white')
    puzzle.add_kropki_dot((2, 7), (2, 8), 'white')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'black')
    puzzle.add_kropki_dot((3, 7), (3, 8), 'white')
    puzzle.add_kropki_dot((4, 0), (4, 1), 'black')
    puzzle.add_kropki_dot((4, 2), (4, 3), 'white')
    puzzle.add_kropki_dot((4, 6), (4, 7), 'white')
    puzzle.add_kropki_dot((5, 5), (5, 6), 'white')
    puzzle.add_kropki_dot((5, 7), (5, 8), 'white')
    puzzle.add_kropki_dot((6, 2), (6, 3), 'white')
    puzzle.add_kropki_dot((6, 7), (6, 8), 'white')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'white')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'black')
    puzzle.add_kropki_dot((0, 4), (1, 4), 'white')
    puzzle.add_kropki_dot((1, 0), (2, 0), 'white')
    puzzle.add_kropki_dot((1, 5), (2, 5), 'white')
    puzzle.add_kropki_dot((2, 1), (3, 1), 'black')
    puzzle.add_kropki_dot((2, 3), (3, 3), 'white')
    puzzle.add_kropki_dot((2, 4), (3, 4), 'black')
    puzzle.add_kropki_dot((3, 1), (4, 1), 'white')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'white')
    puzzle.add_kropki_dot((3, 7), (4, 7), 'black')
    puzzle.add_kropki_dot((4, 0), (5, 0), 'black')
    puzzle.add_kropki_dot((4, 1), (5, 1), 'black')
    puzzle.add_kropki_dot((4, 2), (5, 2), 'white')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'white')
    puzzle.add_kropki_dot((4, 5), (5, 5), 'black')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'white')
    puzzle.add_kropki_dot((6, 0), (7, 0), 'white')
    puzzle.add_kropki_dot((6, 3), (7, 3), 'white')
    puzzle.add_kropki_dot((6, 6), (7, 6), 'black')
    puzzle.add_kropki_dot((7, 3), (8, 3), 'white')
    puzzle.add_kropki_dot((7, 6), (8, 6), 'white')

    return puzzle
