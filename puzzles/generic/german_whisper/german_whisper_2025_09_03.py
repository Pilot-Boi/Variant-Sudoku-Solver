"""PuzzleMadness German Whispers Sudoku — 2025-09-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 5, 0, 7, 0, 0],
        [5, 0, 0, 0, 0, 8, 1, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 6), (8, 5), (7, 5), (7, 6), (7, 7), (6, 6)])
    puzzle.add_german_whispers([(2, 4), (3, 5), (4, 5), (4, 4), (3, 4)])
    puzzle.add_german_whispers([(4, 0), (3, 1), (2, 2), (2, 3), (1, 4)])
    puzzle.add_german_whispers([(5, 4), (5, 3), (5, 2), (6, 1), (6, 2)])
    puzzle.add_german_whispers([(4, 6), (3, 6), (3, 7), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (7, 2), (7, 3)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (1, 0), (1, 1)])

    return puzzle
