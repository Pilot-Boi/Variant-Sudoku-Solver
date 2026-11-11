"""PuzzleMadness German Whispers Sudoku — 2025-10-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 9, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 1, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 8), (4, 8), (5, 7), (6, 7), (6, 8), (7, 7)])
    puzzle.add_german_whispers([(4, 4), (3, 4), (2, 3), (3, 2), (2, 1)])
    puzzle.add_german_whispers([(2, 5), (3, 6), (2, 7), (1, 7), (1, 8)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 6), (1, 5), (2, 4)])
    puzzle.add_german_whispers([(5, 3), (6, 2), (6, 3), (7, 4)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(7, 0), (6, 0), (5, 1), (4, 0)])
    puzzle.add_german_whispers([(6, 5), (7, 6), (8, 6), (8, 5)])
    puzzle.add_german_whispers([(3, 0), (4, 1), (3, 1)])

    return puzzle
