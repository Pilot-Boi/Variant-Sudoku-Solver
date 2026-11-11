"""PuzzleMadness German Whispers Sudoku — 2025-04-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 1],
        [0, 0, 0, 0, 0, 1, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 8), (8, 8), (7, 7), (6, 8), (5, 8), (5, 7)])
    puzzle.add_german_whispers([(1, 2), (2, 1), (1, 1), (0, 0), (1, 0)])
    puzzle.add_german_whispers([(7, 4), (6, 5), (7, 5), (8, 4), (8, 5)])
    puzzle.add_german_whispers([(8, 2), (7, 2), (7, 1), (6, 2), (5, 3)])
    puzzle.add_german_whispers([(3, 7), (2, 7), (2, 6), (1, 7), (1, 6)])
    puzzle.add_german_whispers([(2, 4), (2, 3), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(3, 2), (3, 1), (3, 0), (4, 0)])
    puzzle.add_german_whispers([(2, 2), (1, 3), (0, 3), (1, 4)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (5, 5), (6, 6)])
    puzzle.add_german_whispers([(4, 8), (4, 7), (4, 6)])
    puzzle.add_german_whispers([(6, 1), (5, 0), (6, 0)])

    return puzzle
