"""PuzzleMadness German Whispers Sudoku — 2025-05-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [3, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 2],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 5), (7, 6), (6, 5), (7, 4), (6, 3), (5, 2)])
    puzzle.add_german_whispers([(1, 0), (0, 0), (0, 1), (1, 1), (2, 2)])
    puzzle.add_german_whispers([(1, 2), (2, 3), (2, 4), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(8, 7), (7, 8), (6, 7), (5, 7), (5, 8)])
    puzzle.add_german_whispers([(4, 2), (4, 1), (3, 1), (3, 0), (2, 0)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (0, 6), (1, 6)])
    puzzle.add_german_whispers([(6, 1), (7, 2), (6, 2), (5, 1)])
    puzzle.add_german_whispers([(5, 5), (5, 6), (4, 6), (3, 7)])
    puzzle.add_german_whispers([(1, 3), (0, 3), (1, 4)])

    return puzzle
