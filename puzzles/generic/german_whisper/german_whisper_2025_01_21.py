"""PuzzleMadness German Whispers Sudoku — 2025-01-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 3],
        [0, 0, 2, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 4, 0, 0, 3, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 4), (2, 5), (3, 6), (3, 5), (4, 5), (4, 6)])
    puzzle.add_german_whispers([(6, 3), (6, 2), (5, 1), (4, 0), (3, 0)])
    puzzle.add_german_whispers([(8, 6), (7, 6), (7, 7), (8, 8), (8, 7)])
    puzzle.add_german_whispers([(6, 0), (7, 1), (8, 0), (8, 1), (7, 2)])
    puzzle.add_german_whispers([(4, 4), (3, 3), (2, 2), (2, 3)])
    puzzle.add_german_whispers([(7, 5), (6, 4), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(0, 5), (1, 5), (0, 6), (1, 7)])
    puzzle.add_german_whispers([(1, 1), (0, 2), (0, 1), (1, 0)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (1, 8)])

    return puzzle
