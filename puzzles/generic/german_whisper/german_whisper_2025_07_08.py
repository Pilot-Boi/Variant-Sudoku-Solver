"""PuzzleMadness German Whispers Sudoku — 2025-07-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 1, 0, 0, 2],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 2), (2, 2), (2, 1), (1, 1), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(1, 7), (1, 8), (2, 7), (1, 6), (2, 5)])
    puzzle.add_german_whispers([(4, 3), (3, 4), (4, 4), (4, 5), (3, 6)])
    puzzle.add_german_whispers([(5, 3), (4, 2), (4, 1), (5, 1), (4, 0)])
    puzzle.add_german_whispers([(5, 8), (4, 7), (5, 7), (6, 8)])
    puzzle.add_german_whispers([(7, 2), (6, 1), (7, 1), (7, 0)])
    puzzle.add_german_whispers([(8, 5), (7, 5), (7, 4), (6, 3)])
    puzzle.add_german_whispers([(6, 4), (5, 4), (5, 5)])
    puzzle.add_german_whispers([(1, 4), (1, 5), (0, 5)])

    return puzzle
