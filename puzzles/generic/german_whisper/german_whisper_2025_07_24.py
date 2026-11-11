"""PuzzleMadness German Whispers Sudoku — 2025-07-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 7, 0, 2, 0, 0, 0, 0, 8],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 2), (1, 3), (0, 3), (0, 2), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (2, 8), (2, 7), (2, 6)])
    puzzle.add_german_whispers([(8, 4), (8, 5), (7, 4), (6, 3), (5, 2)])
    puzzle.add_german_whispers([(5, 6), (4, 6), (3, 5), (4, 4), (3, 3)])
    puzzle.add_german_whispers([(6, 6), (7, 6), (6, 7), (7, 7), (6, 8)])
    puzzle.add_german_whispers([(5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_german_whispers([(7, 2), (6, 1), (7, 1), (7, 0)])
    puzzle.add_german_whispers([(2, 5), (1, 5), (1, 6), (0, 7)])
    puzzle.add_german_whispers([(3, 1), (4, 0), (3, 0)])

    return puzzle
