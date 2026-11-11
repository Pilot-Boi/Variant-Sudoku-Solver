"""PuzzleMadness Kropki Sudoku — 2025-06-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Kropki Sudoku — 2025-06-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/kropkisudoku/hard/2025/6/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_kropki_dot((0, 0), (0, 1), 'white')
    puzzle.add_kropki_dot((0, 2), (0, 3), 'black')
    puzzle.add_kropki_dot((0, 5), (0, 6), 'black')
    puzzle.add_kropki_dot((1, 0), (1, 1), 'white')
    puzzle.add_kropki_dot((1, 3), (1, 4), 'black')
    puzzle.add_kropki_dot((2, 0), (2, 1), 'white')
    puzzle.add_kropki_dot((2, 5), (2, 6), 'black')
    puzzle.add_kropki_dot((3, 2), (3, 3), 'black')
    puzzle.add_kropki_dot((3, 3), (3, 4), 'black')
    puzzle.add_kropki_dot((4, 0), (4, 1), 'white')
    puzzle.add_kropki_dot((4, 4), (4, 5), 'white')
    puzzle.add_kropki_dot((4, 6), (4, 7), 'black')
    puzzle.add_kropki_dot((4, 7), (4, 8), 'white')
    puzzle.add_kropki_dot((5, 1), (5, 2), 'white')
    puzzle.add_kropki_dot((5, 4), (5, 5), 'white')
    puzzle.add_kropki_dot((5, 6), (5, 7), 'black')
    puzzle.add_kropki_dot((6, 3), (6, 4), 'black')
    puzzle.add_kropki_dot((6, 5), (6, 6), 'black')
    puzzle.add_kropki_dot((6, 7), (6, 8), 'white')
    puzzle.add_kropki_dot((7, 7), (7, 8), 'white')
    puzzle.add_kropki_dot((8, 0), (8, 1), 'white')
    puzzle.add_kropki_dot((8, 3), (8, 4), 'black')
    puzzle.add_kropki_dot((8, 5), (8, 6), 'white')
    puzzle.add_kropki_dot((0, 2), (1, 2), 'black')
    puzzle.add_kropki_dot((0, 4), (1, 4), 'white')
    puzzle.add_kropki_dot((0, 6), (1, 6), 'white')
    puzzle.add_kropki_dot((1, 5), (2, 5), 'white')
    puzzle.add_kropki_dot((1, 7), (2, 7), 'white')
    puzzle.add_kropki_dot((2, 4), (3, 4), 'white')
    puzzle.add_kropki_dot((2, 5), (3, 5), 'black')
    puzzle.add_kropki_dot((3, 6), (4, 6), 'white')
    puzzle.add_kropki_dot((4, 0), (5, 0), 'white')
    puzzle.add_kropki_dot((4, 2), (5, 2), 'white')
    puzzle.add_kropki_dot((4, 8), (5, 8), 'black')
    puzzle.add_kropki_dot((5, 5), (6, 5), 'white')
    puzzle.add_kropki_dot((6, 0), (7, 0), 'black')
    puzzle.add_kropki_dot((6, 2), (7, 2), 'white')
    puzzle.add_kropki_dot((7, 3), (8, 3), 'white')
    puzzle.add_kropki_dot((7, 5), (8, 5), 'white')
    puzzle.add_kropki_dot((7, 7), (8, 7), 'black')

    return puzzle
