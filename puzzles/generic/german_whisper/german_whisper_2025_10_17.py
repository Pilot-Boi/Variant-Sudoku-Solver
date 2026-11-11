"""PuzzleMadness German Whispers Sudoku — 2025-10-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 5, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 4), (7, 3), (6, 2), (6, 3), (7, 4), (6, 4)])
    puzzle.add_german_whispers([(3, 3), (4, 2), (5, 1), (4, 1), (4, 0)])
    puzzle.add_german_whispers([(5, 6), (4, 6), (3, 5), (2, 6), (2, 7)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (0, 5), (1, 4), (1, 5)])
    puzzle.add_german_whispers([(7, 2), (6, 1), (6, 0), (7, 1)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (5, 7), (6, 7)])
    puzzle.add_german_whispers([(7, 8), (8, 7), (7, 7), (7, 6)])
    puzzle.add_german_whispers([(4, 4), (5, 4), (6, 5)])
    puzzle.add_german_whispers([(1, 1), (0, 2), (1, 2)])

    return puzzle
