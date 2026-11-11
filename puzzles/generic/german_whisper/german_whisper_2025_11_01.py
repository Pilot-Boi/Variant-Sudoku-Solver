"""PuzzleMadness German Whispers Sudoku — 2025-11-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 3, 0, 0],
        [0, 4, 0, 0, 0, 7, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 4), (2, 4), (2, 3), (1, 4), (1, 5), (0, 4)])
    puzzle.add_german_whispers([(5, 1), (4, 1), (4, 0), (3, 0), (2, 1)])
    puzzle.add_german_whispers([(7, 6), (6, 5), (5, 5), (6, 4), (7, 5)])
    puzzle.add_german_whispers([(5, 8), (4, 7), (3, 6), (3, 7), (4, 8)])
    puzzle.add_german_whispers([(8, 1), (8, 2), (7, 3), (7, 4), (8, 3)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(0, 1), (0, 2), (0, 3), (1, 3)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (6, 2), (7, 1)])
    puzzle.add_german_whispers([(4, 2), (3, 3), (3, 2)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (7, 8)])

    return puzzle
