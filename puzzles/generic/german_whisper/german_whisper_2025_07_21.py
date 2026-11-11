"""PuzzleMadness German Whispers Sudoku — 2025-07-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 3, 0, 0, 9, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 1), (5, 2), (6, 3), (7, 3), (6, 2), (6, 1)])
    puzzle.add_german_whispers([(4, 4), (3, 5), (4, 5), (5, 6), (6, 6)])
    puzzle.add_german_whispers([(4, 8), (3, 8), (2, 8), (2, 7), (1, 7)])
    puzzle.add_german_whispers([(0, 5), (1, 5), (1, 4), (0, 3), (1, 2)])
    puzzle.add_german_whispers([(7, 7), (7, 6), (8, 5), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(3, 0), (2, 1), (2, 0), (1, 1)])
    puzzle.add_german_whispers([(3, 3), (3, 4), (2, 3), (2, 2)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (7, 1)])
    puzzle.add_german_whispers([(4, 2), (4, 3), (5, 3)])

    return puzzle
