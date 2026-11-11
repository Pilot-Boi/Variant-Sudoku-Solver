"""PuzzleMadness German Whispers Sudoku — 2025-05-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 1, 5, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 8, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 8), (1, 7), (2, 6), (3, 5), (3, 6), (2, 7)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (2, 1), (3, 1), (4, 1)])
    puzzle.add_german_whispers([(5, 5), (6, 4), (7, 3), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(6, 2), (6, 3), (5, 2), (4, 2), (3, 3)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (7, 7), (7, 8), (6, 7)])
    puzzle.add_german_whispers([(3, 4), (2, 3), (1, 2), (1, 1)])
    puzzle.add_german_whispers([(4, 5), (4, 6), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(1, 5), (2, 4), (1, 4)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (0, 8)])

    return puzzle
