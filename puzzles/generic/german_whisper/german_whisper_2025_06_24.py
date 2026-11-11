"""PuzzleMadness German Whispers Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [7, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 8), (6, 7), (5, 7), (6, 6), (5, 5), (4, 4)])
    puzzle.add_german_whispers([(7, 1), (8, 1), (8, 0), (7, 0), (6, 1)])
    puzzle.add_german_whispers([(1, 1), (2, 1), (2, 2), (3, 2), (2, 3)])
    puzzle.add_german_whispers([(6, 3), (5, 2), (4, 2), (4, 3), (5, 4)])
    puzzle.add_german_whispers([(0, 4), (1, 5), (0, 6), (0, 7)])
    puzzle.add_german_whispers([(4, 7), (3, 6), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(2, 4), (1, 3), (0, 2)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (1, 8)])

    return puzzle
