"""PuzzleMadness German Whispers Sudoku — 2025-07-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 5, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 8, 6, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [1, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 5), (6, 4), (5, 3), (6, 2), (7, 2), (7, 1)])
    puzzle.add_german_whispers([(2, 8), (3, 7), (4, 7), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(4, 0), (5, 1), (4, 1), (3, 2), (3, 1)])
    puzzle.add_german_whispers([(2, 2), (1, 2), (1, 3), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(2, 5), (1, 5), (1, 6), (0, 7)])
    puzzle.add_german_whispers([(5, 5), (5, 4), (4, 4), (3, 5)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (0, 1)])

    return puzzle
