"""PuzzleMadness Kropki Sudoku — 2025-12-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-12-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/12/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 2), (0, 3), 'black')
    puzzle.add_kropki_dot((0, 7), (0, 8), 'white')
    puzzle.add_kropki_dot((1, 7), (1, 8), 'white')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'black')
    puzzle.add_kropki_dot((3, 0), (3, 1), 'white')
    puzzle.add_kropki_dot((3, 1), (3, 2), 'black')
    puzzle.add_kropki_dot((4, 5), (4, 6), 'black')
    puzzle.add_kropki_dot((4, 6), (4, 7), 'white')
    puzzle.add_kropki_dot((4, 7), (4, 8), 'white')
    puzzle.add_kropki_dot((5, 1), (5, 2), 'black')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'white')
    puzzle.add_kropki_dot((5, 6), (5, 7), 'white')
    puzzle.add_kropki_dot((6, 4), (6, 5), 'white')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'black')
    puzzle.add_kropki_dot((8, 0), (8, 1), 'white')
    puzzle.add_kropki_dot((0, 1), (1, 1), 'white')
    puzzle.add_kropki_dot((0, 2), (1, 2), 'black')
    puzzle.add_kropki_dot((1, 2), (2, 2), 'black')
    puzzle.add_kropki_dot((1, 8), (2, 8), 'white')
    puzzle.add_kropki_dot((2, 2), (3, 2), 'black')
    puzzle.add_kropki_dot((3, 1), (4, 1), 'black')
    puzzle.add_kropki_dot((3, 2), (4, 2), 'white')
    puzzle.add_kropki_dot((3, 4), (4, 4), 'white')
    puzzle.add_kropki_dot((3, 5), (4, 5), 'white')
    puzzle.add_kropki_dot((3, 6), (4, 6), 'white')
    puzzle.add_kropki_dot((4, 1), (5, 1), 'white')
    puzzle.add_kropki_dot((4, 2), (5, 2), 'white')
    puzzle.add_kropki_dot((5, 2), (6, 2), 'white')
    puzzle.add_kropki_dot((5, 5), (6, 5), 'white')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'black')
    puzzle.add_kropki_dot((6, 1), (7, 1), 'white')
    puzzle.add_kropki_dot((6, 4), (7, 4), 'white')
    puzzle.add_kropki_dot((6, 8), (7, 8), 'white')
    puzzle.add_kropki_dot((7, 0), (8, 0), 'black')
    puzzle.add_kropki_dot((7, 4), (8, 4), 'black')
    puzzle.add_kropki_dot((7, 5), (8, 5), 'black')
    puzzle.add_kropki_dot((7, 6), (8, 6), 'white')

    return puzzle
