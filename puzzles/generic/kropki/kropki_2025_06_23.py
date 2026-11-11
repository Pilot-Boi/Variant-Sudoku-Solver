"""PuzzleMadness Kropki Sudoku — 2025-06-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-06-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/6/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 5), (0, 6), 'white')
    puzzle.add_kropki_dot((1, 0), (1, 1), 'white')
    puzzle.add_kropki_dot((1, 2), (1, 3), 'white')
    puzzle.add_kropki_dot((1, 5), (1, 6), 'white')
    puzzle.add_kropki_dot((2, 5), (2, 6), 'white')
    puzzle.add_kropki_dot((3, 1), (3, 2), 'white')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'white')
    puzzle.add_kropki_dot((4, 2), (4, 3), 'white')
    puzzle.add_kropki_dot((5, 2), (5, 3), 'white')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'white')
    puzzle.add_kropki_dot((5, 5), (5, 6), 'black')
    puzzle.add_kropki_dot((5, 6), (5, 7), 'white')
    puzzle.add_kropki_dot((6, 4), (6, 5), 'white')
    puzzle.add_kropki_dot((6, 5), (6, 6), 'white')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 3), (8, 4), 'white')
    puzzle.add_kropki_dot((8, 6), (8, 7), 'white')
    puzzle.add_kropki_dot((0, 1), (1, 1), 'white')
    puzzle.add_kropki_dot((0, 2), (1, 2), 'black')
    puzzle.add_kropki_dot((0, 3), (1, 3), 'black')
    puzzle.add_kropki_dot((0, 6), (1, 6), 'black')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'black')
    puzzle.add_kropki_dot((2, 2), (3, 2), 'black')
    puzzle.add_kropki_dot((2, 4), (3, 4), 'black')
    puzzle.add_kropki_dot((2, 8), (3, 8), 'white')
    puzzle.add_kropki_dot((3, 0), (4, 0), 'white')
    puzzle.add_kropki_dot((3, 1), (4, 1), 'black')
    puzzle.add_kropki_dot((3, 7), (4, 7), 'white')
    puzzle.add_kropki_dot((4, 2), (5, 2), 'white')
    puzzle.add_kropki_dot((4, 3), (5, 3), 'white')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'white')
    puzzle.add_kropki_dot((4, 5), (5, 5), 'white')
    puzzle.add_kropki_dot((4, 6), (5, 6), 'black')
    puzzle.add_kropki_dot((5, 0), (6, 0), 'black')
    puzzle.add_kropki_dot((5, 1), (6, 1), 'white')
    puzzle.add_kropki_dot((5, 4), (6, 4), 'white')
    puzzle.add_kropki_dot((5, 5), (6, 5), 'black')
    puzzle.add_kropki_dot((6, 1), (7, 1), 'black')
    puzzle.add_kropki_dot((6, 3), (7, 3), 'white')
    puzzle.add_kropki_dot((6, 8), (7, 8), 'white')
    puzzle.add_kropki_dot((7, 0), (8, 0), 'black')

    return puzzle
