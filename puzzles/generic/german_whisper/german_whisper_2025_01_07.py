"""PuzzleMadness German Whispers Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 7, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 4), (3, 5), (3, 6), (4, 6), (5, 6), (5, 5)])
    puzzle.add_german_whispers([(7, 6), (7, 7), (7, 8), (8, 7), (8, 8)])
    puzzle.add_german_whispers([(5, 2), (6, 2), (5, 1), (4, 2), (3, 2)])
    puzzle.add_german_whispers([(1, 3), (0, 3), (1, 2), (2, 2), (3, 1)])
    puzzle.add_german_whispers([(3, 7), (2, 8), (2, 7), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(5, 4), (6, 4), (6, 5), (7, 4)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (7, 2), (7, 3)])
    puzzle.add_german_whispers([(0, 0), (1, 1), (2, 0), (3, 0)])
    puzzle.add_german_whispers([(5, 8), (4, 8), (5, 7)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0)])

    return puzzle
