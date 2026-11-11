"""PuzzleMadness German Whispers Sudoku — 2025-05-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 7), (7, 8), (6, 8), (6, 7), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(1, 6), (2, 7), (2, 6), (3, 6), (3, 5)])
    puzzle.add_german_whispers([(4, 6), (4, 5), (3, 4), (2, 3), (1, 2)])
    puzzle.add_german_whispers([(4, 3), (3, 2), (2, 1), (2, 0), (3, 0)])
    puzzle.add_german_whispers([(0, 4), (0, 3), (0, 2), (0, 1), (0, 0)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (8, 1), (7, 2)])
    puzzle.add_german_whispers([(6, 4), (6, 3), (7, 4), (8, 5)])
    puzzle.add_german_whispers([(7, 6), (6, 5), (5, 5), (5, 4)])

    return puzzle
