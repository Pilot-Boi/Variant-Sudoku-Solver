"""PuzzleMadness German Whispers Sudoku — 2025-05-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [7, 0, 5, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 2, 0, 0, 1, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 5), (5, 5), (6, 6), (7, 7), (8, 8), (8, 7)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (1, 6), (2, 7), (3, 7)])
    puzzle.add_german_whispers([(7, 4), (6, 4), (5, 3), (6, 2), (5, 1)])
    puzzle.add_german_whispers([(1, 1), (2, 0), (3, 0), (4, 0), (3, 1)])
    puzzle.add_german_whispers([(4, 7), (3, 6), (2, 5), (2, 6)])
    puzzle.add_german_whispers([(3, 5), (4, 6), (5, 7), (5, 8)])
    puzzle.add_german_whispers([(8, 1), (7, 1), (7, 2), (8, 2)])
    puzzle.add_german_whispers([(0, 3), (1, 3), (2, 2), (2, 3)])
    puzzle.add_german_whispers([(5, 4), (4, 4), (3, 4)])

    return puzzle
