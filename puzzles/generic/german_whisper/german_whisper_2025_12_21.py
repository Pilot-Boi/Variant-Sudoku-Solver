"""PuzzleMadness German Whispers Sudoku — 2025-12-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 7, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 8],
        [3, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 4), (5, 4), (4, 5), (3, 5), (3, 6), (4, 7)])
    puzzle.add_german_whispers([(5, 2), (5, 1), (4, 0), (3, 1), (2, 2)])
    puzzle.add_german_whispers([(7, 4), (7, 5), (6, 6), (7, 6), (8, 5)])
    puzzle.add_german_whispers([(4, 8), (3, 8), (2, 7), (2, 8), (1, 7)])
    puzzle.add_german_whispers([(1, 3), (1, 4), (2, 3), (3, 2)])
    puzzle.add_german_whispers([(6, 0), (7, 1), (6, 1), (7, 2)])
    puzzle.add_german_whispers([(0, 1), (0, 0), (1, 1), (0, 2)])
    puzzle.add_german_whispers([(5, 3), (6, 4), (6, 3)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (7, 7)])

    return puzzle
