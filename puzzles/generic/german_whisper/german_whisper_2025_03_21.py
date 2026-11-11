"""PuzzleMadness German Whispers Sudoku — 2025-03-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 3), (4, 3), (5, 4), (5, 5), (4, 5), (3, 6)])
    puzzle.add_german_whispers([(4, 1), (3, 2), (2, 1), (3, 0), (2, 0)])
    puzzle.add_german_whispers([(6, 7), (5, 7), (6, 8), (7, 8), (7, 7)])
    puzzle.add_german_whispers([(7, 1), (6, 1), (7, 2), (6, 2), (6, 3)])
    puzzle.add_german_whispers([(0, 7), (1, 7), (2, 8), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(8, 4), (8, 5), (7, 4), (8, 3)])
    puzzle.add_german_whispers([(2, 5), (2, 6), (1, 5), (0, 5)])
    puzzle.add_german_whispers([(1, 1), (1, 2), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(1, 3), (0, 4), (0, 3)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (8, 0)])

    return puzzle
