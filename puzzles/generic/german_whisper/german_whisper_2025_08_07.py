"""PuzzleMadness German Whispers Sudoku — 2025-08-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 3, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 2, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 8), (5, 7), (4, 7), (5, 6), (6, 6), (6, 7)])
    puzzle.add_german_whispers([(5, 2), (6, 1), (6, 2), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(2, 6), (1, 5), (2, 4), (3, 5), (4, 4)])
    puzzle.add_german_whispers([(0, 1), (0, 0), (1, 0), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(3, 2), (4, 2), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(7, 2), (7, 3), (8, 4), (7, 5)])
    puzzle.add_german_whispers([(0, 6), (0, 7), (1, 7), (2, 8)])
    puzzle.add_german_whispers([(2, 7), (3, 7), (4, 6)])
    puzzle.add_german_whispers([(0, 4), (0, 3), (1, 4)])
    puzzle.add_german_whispers([(8, 6), (8, 5), (7, 6)])

    return puzzle
