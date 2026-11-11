"""PuzzleMadness German Whispers Sudoku — 2025-11-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 1],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 0, 8, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 5), (4, 5), (4, 6), (3, 6), (2, 5), (1, 4)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (4, 2), (4, 1), (5, 1)])
    puzzle.add_german_whispers([(4, 0), (3, 0), (2, 1), (2, 0), (1, 1)])
    puzzle.add_german_whispers([(6, 4), (5, 5), (6, 6), (7, 7), (8, 8)])
    puzzle.add_german_whispers([(8, 5), (7, 5), (8, 4), (7, 4), (8, 3)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (6, 2), (7, 1)])
    puzzle.add_german_whispers([(0, 1), (1, 2), (1, 3), (0, 4)])
    puzzle.add_german_whispers([(2, 8), (1, 8), (2, 7)])

    return puzzle
