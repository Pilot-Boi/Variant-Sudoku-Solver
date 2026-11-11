"""PuzzleMadness Kropki Sudoku — 2025-03-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-03-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/3/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 0), (0, 1), 'black')
    puzzle.add_kropki_dot((0, 5), (0, 6), 'white')
    puzzle.add_kropki_dot((1, 3), (1, 4), 'white')
    puzzle.add_kropki_dot((1, 7), (1, 8), 'white')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 2), (2, 3), 'white')
    puzzle.add_kropki_dot((2, 3), (2, 4), 'black')
    puzzle.add_kropki_dot((2, 4), (2, 5), 'white')
    puzzle.add_kropki_dot((3, 2), (3, 3), 'white')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'white')
    puzzle.add_kropki_dot((4, 3), (4, 4), 'black')
    puzzle.add_kropki_dot((4, 5), (4, 6), 'white')
    puzzle.add_kropki_dot((4, 6), (4, 7), 'black')
    puzzle.add_kropki_dot((5, 1), (5, 2), 'white')
    puzzle.add_kropki_dot((6, 2), (6, 3), 'black')
    puzzle.add_kropki_dot((6, 3), (6, 4), 'white')
    puzzle.add_kropki_dot((6, 5), (6, 6), 'black')
    puzzle.add_kropki_dot((6, 6), (6, 7), 'white')
    puzzle.add_kropki_dot((6, 7), (6, 8), 'white')
    puzzle.add_kropki_dot((7, 2), (7, 3), 'white')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 4), (8, 5), 'black')
    puzzle.add_kropki_dot((8, 6), (8, 7), 'white')
    puzzle.add_kropki_dot((0, 5), (1, 5), 'white')
    puzzle.add_kropki_dot((1, 1), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 3), (3, 3), 'white')
    puzzle.add_kropki_dot((2, 4), (3, 4), 'black')
    puzzle.add_kropki_dot((2, 8), (3, 8), 'white')
    puzzle.add_kropki_dot((3, 3), (4, 3), 'white')
    puzzle.add_kropki_dot((3, 7), (4, 7), 'white')
    puzzle.add_kropki_dot((3, 8), (4, 8), 'black')
    puzzle.add_kropki_dot((4, 6), (5, 6), 'white')
    puzzle.add_kropki_dot((4, 7), (5, 7), 'white')
    puzzle.add_kropki_dot((4, 8), (5, 8), 'white')
    puzzle.add_kropki_dot((5, 2), (6, 2), 'white')
    puzzle.add_kropki_dot((5, 3), (6, 3), 'white')
    puzzle.add_kropki_dot((5, 8), (6, 8), 'white')
    puzzle.add_kropki_dot((6, 1), (7, 1), 'white')
    puzzle.add_kropki_dot((6, 2), (7, 2), 'black')
    puzzle.add_kropki_dot((6, 3), (7, 3), 'white')
    puzzle.add_kropki_dot((6, 7), (7, 7), 'black')
    puzzle.add_kropki_dot((7, 1), (8, 1), 'black')
    puzzle.add_kropki_dot((7, 4), (8, 4), 'white')

    return puzzle
