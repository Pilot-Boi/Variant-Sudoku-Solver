"""PuzzleMadness German Whispers Sudoku — 2025-04-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 8), (2, 7), (3, 7), (4, 8), (4, 7), (5, 8)])
    puzzle.add_german_whispers([(7, 7), (6, 7), (6, 6), (7, 5), (8, 5)])
    puzzle.add_german_whispers([(5, 2), (5, 1), (4, 2), (4, 3), (5, 3)])
    puzzle.add_german_whispers([(0, 5), (1, 5), (2, 5), (2, 6), (3, 6)])
    puzzle.add_german_whispers([(4, 5), (5, 5), (5, 4), (6, 4), (7, 4)])
    puzzle.add_german_whispers([(8, 0), (7, 0), (6, 1), (5, 0)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(2, 2), (1, 2), (1, 3), (2, 3)])
    puzzle.add_german_whispers([(3, 0), (3, 1), (4, 1)])

    return puzzle
