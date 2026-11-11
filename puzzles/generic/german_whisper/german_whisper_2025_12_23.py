"""PuzzleMadness German Whispers Sudoku — 2025-12-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [3, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 9, 0],
        [0, 7, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 5), (8, 5), (7, 4), (7, 3), (7, 2), (8, 1)])
    puzzle.add_german_whispers([(4, 4), (5, 5), (5, 6), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(1, 5), (2, 5), (3, 6), (3, 7), (2, 8)])
    puzzle.add_german_whispers([(1, 1), (1, 2), (1, 3), (2, 3), (2, 2)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (7, 1), (6, 1), (6, 0)])
    puzzle.add_german_whispers([(3, 3), (4, 3), (4, 2), (5, 1)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (0, 6), (1, 7)])

    return puzzle
