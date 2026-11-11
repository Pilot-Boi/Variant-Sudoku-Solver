"""PuzzleMadness German Whispers Sudoku — 2025-11-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 4, 0, 0],
        [4, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 5), (2, 4), (1, 5), (0, 5), (1, 4), (1, 3)])
    puzzle.add_german_whispers([(2, 1), (3, 2), (3, 3), (4, 4), (4, 3)])
    puzzle.add_german_whispers([(6, 2), (7, 3), (8, 4), (8, 5), (7, 4)])
    puzzle.add_german_whispers([(7, 7), (6, 8), (5, 7), (4, 6), (5, 6)])
    puzzle.add_german_whispers([(2, 7), (2, 6), (3, 7), (4, 8)])
    puzzle.add_german_whispers([(6, 1), (5, 2), (5, 1), (4, 0)])
    puzzle.add_german_whispers([(0, 2), (1, 1), (0, 1), (1, 0)])

    return puzzle
