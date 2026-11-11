"""PuzzleMadness German Whispers Sudoku — 2025-06-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 8, 3, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 2, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 6, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 3), (4, 4), (4, 5), (5, 5), (6, 6), (5, 7)])
    puzzle.add_german_whispers([(4, 3), (3, 2), (4, 2), (4, 1), (5, 2)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (7, 3), (8, 4), (7, 4)])
    puzzle.add_german_whispers([(3, 7), (2, 6), (2, 7), (1, 8), (2, 8)])
    puzzle.add_german_whispers([(1, 3), (0, 2), (0, 1), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(8, 6), (8, 5), (7, 6), (6, 7)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(4, 7), (3, 6), (2, 5)])

    return puzzle
