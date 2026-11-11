"""PuzzleMadness German Whispers Sudoku — 2025-04-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 3, 4, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 3), (2, 2), (3, 2), (4, 3), (4, 4), (5, 3)])
    puzzle.add_german_whispers([(5, 6), (5, 7), (4, 6), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(4, 2), (4, 1), (5, 0), (6, 0), (5, 1)])
    puzzle.add_german_whispers([(5, 2), (6, 1), (7, 0), (8, 0), (7, 1)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (2, 6), (1, 7)])
    puzzle.add_german_whispers([(6, 3), (7, 4), (7, 3), (8, 2)])
    puzzle.add_german_whispers([(7, 5), (8, 6), (8, 7), (8, 8)])
    puzzle.add_german_whispers([(2, 4), (3, 4), (2, 5), (1, 4)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (0, 1)])
    puzzle.add_german_whispers([(0, 5), (1, 5), (0, 4)])
    puzzle.add_german_whispers([(1, 8), (0, 8), (0, 7)])

    return puzzle
