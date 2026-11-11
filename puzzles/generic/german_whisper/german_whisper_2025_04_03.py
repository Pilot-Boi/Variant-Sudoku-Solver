"""PuzzleMadness German Whispers Sudoku — 2025-04-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 0, 0],
        [7, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 8, 0, 1, 0, 0, 6],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 1), (7, 0), (7, 1), (6, 1), (5, 1), (6, 0)])
    puzzle.add_german_whispers([(1, 2), (0, 1), (0, 2), (1, 3), (0, 3)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (2, 7), (3, 8), (2, 8)])
    puzzle.add_german_whispers([(7, 6), (6, 6), (6, 5), (7, 4), (6, 4)])
    puzzle.add_german_whispers([(0, 6), (1, 5), (2, 5), (2, 6)])
    puzzle.add_german_whispers([(3, 2), (4, 3), (5, 4), (4, 5)])
    puzzle.add_german_whispers([(4, 4), (3, 5), (3, 6)])
    puzzle.add_german_whispers([(2, 0), (3, 0), (4, 1)])
    puzzle.add_german_whispers([(8, 8), (7, 7), (7, 8)])

    return puzzle
