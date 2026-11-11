"""PuzzleMadness German Whispers Sudoku — 2025-01-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 3, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [1, 8, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 1), (5, 1), (6, 2), (7, 3), (8, 4), (7, 4)])
    puzzle.add_german_whispers([(2, 1), (1, 2), (2, 2), (3, 1), (4, 2)])
    puzzle.add_german_whispers([(3, 7), (2, 7), (1, 7), (1, 8), (0, 8)])
    puzzle.add_german_whispers([(7, 6), (6, 6), (6, 7), (6, 8), (5, 8)])
    puzzle.add_german_whispers([(4, 3), (3, 3), (3, 4), (4, 4), (5, 4)])
    puzzle.add_german_whispers([(1, 4), (0, 3), (1, 3), (2, 3)])
    puzzle.add_german_whispers([(5, 6), (5, 7), (4, 6), (4, 7)])
    puzzle.add_german_whispers([(2, 5), (1, 5), (1, 6), (0, 7)])
    puzzle.add_german_whispers([(5, 0), (4, 0), (3, 0)])

    return puzzle
