"""PuzzleMadness German Whispers Sudoku — 2025-09-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 6, 0, 8],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 5],
        [0, 9, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 5), (6, 6), (6, 5), (7, 4), (7, 3), (8, 3)])
    puzzle.add_german_whispers([(1, 2), (2, 1), (2, 0), (3, 0), (4, 0)])
    puzzle.add_german_whispers([(2, 6), (2, 5), (1, 6), (1, 5), (0, 5)])
    puzzle.add_german_whispers([(4, 6), (5, 7), (5, 8), (6, 7), (7, 7)])
    puzzle.add_german_whispers([(4, 1), (4, 2), (4, 3), (3, 3), (3, 4)])
    puzzle.add_german_whispers([(1, 8), (2, 7), (1, 7), (0, 8)])
    puzzle.add_german_whispers([(7, 1), (6, 2), (6, 3), (5, 3)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(3, 6), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(7, 5), (7, 6), (8, 6)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0)])

    return puzzle
