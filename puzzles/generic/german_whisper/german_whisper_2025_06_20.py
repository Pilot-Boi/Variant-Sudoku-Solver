"""PuzzleMadness German Whispers Sudoku — 2025-06-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 6, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 1, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 4), (6, 5), (5, 5), (5, 4), (6, 3), (6, 2)])
    puzzle.add_german_whispers([(4, 7), (3, 6), (2, 5), (3, 5), (3, 4)])
    puzzle.add_german_whispers([(3, 7), (2, 7), (1, 6), (0, 7), (0, 6)])
    puzzle.add_german_whispers([(1, 1), (2, 2), (2, 1), (3, 2), (4, 2)])
    puzzle.add_german_whispers([(8, 5), (8, 6), (8, 7), (8, 8), (7, 7)])
    puzzle.add_german_whispers([(6, 4), (7, 3), (7, 2), (6, 1)])
    puzzle.add_german_whispers([(1, 2), (0, 3), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(5, 2), (4, 1), (5, 1), (5, 0)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (1, 8)])
    puzzle.add_german_whispers([(1, 4), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(0, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(7, 8), (6, 8), (5, 8)])

    return puzzle
