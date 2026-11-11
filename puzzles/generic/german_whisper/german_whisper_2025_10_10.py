"""PuzzleMadness German Whispers Sudoku — 2025-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 9, 2, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 0), (3, 1), (2, 0), (1, 1), (2, 2), (1, 3)])
    puzzle.add_german_whispers([(7, 7), (8, 6), (8, 5), (7, 4), (8, 3)])
    puzzle.add_german_whispers([(7, 0), (6, 1), (7, 1), (6, 2), (6, 3)])
    puzzle.add_german_whispers([(4, 1), (4, 2), (3, 3), (4, 4), (4, 3)])
    puzzle.add_german_whispers([(4, 6), (3, 5), (3, 6), (4, 7)])
    puzzle.add_german_whispers([(0, 5), (1, 4), (1, 5), (2, 4)])
    puzzle.add_german_whispers([(1, 6), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(6, 4), (6, 5), (7, 5)])
    puzzle.add_german_whispers([(6, 8), (5, 8), (4, 8)])

    return puzzle
