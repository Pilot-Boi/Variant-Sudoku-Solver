"""PuzzleMadness German Whispers Sudoku — 2025-04-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [3, 0, 0, 0, 4, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 6), (2, 7), (1, 8), (1, 7), (0, 6), (0, 7)])
    puzzle.add_german_whispers([(4, 8), (3, 7), (4, 6), (5, 7), (6, 8)])
    puzzle.add_german_whispers([(4, 0), (3, 0), (2, 1), (2, 2), (1, 3)])
    puzzle.add_german_whispers([(8, 6), (7, 7), (7, 6), (6, 7), (5, 6)])
    puzzle.add_german_whispers([(6, 4), (6, 3), (5, 2), (5, 1)])
    puzzle.add_german_whispers([(5, 5), (5, 4), (4, 4), (3, 5)])
    puzzle.add_german_whispers([(6, 1), (7, 2), (8, 1), (7, 1)])
    puzzle.add_german_whispers([(7, 3), (8, 3), (7, 4), (8, 5)])
    puzzle.add_german_whispers([(2, 5), (1, 5), (1, 6)])

    return puzzle
