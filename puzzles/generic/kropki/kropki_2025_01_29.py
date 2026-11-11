"""PuzzleMadness Kropki Sudoku — 2025-01-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-01-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/1/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 1), (0, 2), 'white')
    puzzle.add_kropki_dot((0, 3), (0, 4), 'white')
    puzzle.add_kropki_dot((0, 4), (0, 5), 'white')
    puzzle.add_kropki_dot((0, 6), (0, 7), 'white')
    puzzle.add_kropki_dot((1, 3), (1, 4), 'white')
    puzzle.add_kropki_dot((1, 4), (1, 5), 'black')
    puzzle.add_kropki_dot((3, 1), (3, 2), 'white')
    puzzle.add_kropki_dot((3, 4), (3, 5), 'white')
    puzzle.add_kropki_dot((3, 5), (3, 6), 'white')
    puzzle.add_kropki_dot((3, 7), (3, 8), 'white')
    puzzle.add_kropki_dot((4, 0), (4, 1), 'white')
    puzzle.add_kropki_dot((4, 1), (4, 2), 'black')
    puzzle.add_kropki_dot((4, 2), (4, 3), 'black')
    puzzle.add_kropki_dot((4, 4), (4, 5), 'black')
    puzzle.add_kropki_dot((5, 3), (5, 4), 'white')
    puzzle.add_kropki_dot((5, 6), (5, 7), 'black')
    puzzle.add_kropki_dot((6, 0), (6, 1), 'white')
    puzzle.add_kropki_dot((7, 1), (7, 2), 'white')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 6), (8, 7), 'white')
    puzzle.add_kropki_dot((0, 0), (1, 0), 'white')
    puzzle.add_kropki_dot((0, 4), (1, 4), 'black')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'white')
    puzzle.add_kropki_dot((1, 8), (2, 8), 'white')
    puzzle.add_kropki_dot((2, 8), (3, 8), 'black')
    puzzle.add_kropki_dot((3, 1), (4, 1), 'white')
    puzzle.add_kropki_dot((3, 3), (4, 3), 'black')
    puzzle.add_kropki_dot((3, 4), (4, 4), 'white')
    puzzle.add_kropki_dot((3, 5), (4, 5), 'white')
    puzzle.add_kropki_dot((4, 2), (5, 2), 'white')
    puzzle.add_kropki_dot((4, 4), (5, 4), 'white')
    puzzle.add_kropki_dot((5, 0), (6, 0), 'white')
    puzzle.add_kropki_dot((5, 3), (6, 3), 'white')
    puzzle.add_kropki_dot((5, 6), (6, 6), 'black')
    puzzle.add_kropki_dot((6, 0), (7, 0), 'black')
    puzzle.add_kropki_dot((6, 1), (7, 1), 'white')
    puzzle.add_kropki_dot((6, 7), (7, 7), 'black')
    puzzle.add_kropki_dot((7, 1), (8, 1), 'black')
    puzzle.add_kropki_dot((7, 7), (8, 7), 'white')

    return puzzle
