"""PuzzleMadness German Whispers Sudoku — 2025-09-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 7, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 3, 0, 9, 0, 8, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 7), (5, 6), (4, 6), (3, 5), (2, 4), (3, 4)])
    puzzle.add_german_whispers([(5, 5), (4, 4), (5, 4), (6, 4), (6, 5)])
    puzzle.add_german_whispers([(7, 3), (8, 3), (8, 2), (8, 1), (7, 2)])
    puzzle.add_german_whispers([(1, 4), (0, 3), (1, 3), (1, 2), (2, 1)])
    puzzle.add_german_whispers([(2, 7), (2, 8), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 5), (2, 6)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (8, 7)])
    puzzle.add_german_whispers([(4, 1), (5, 0), (6, 0)])
    puzzle.add_german_whispers([(8, 6), (7, 6), (7, 5)])

    return puzzle
