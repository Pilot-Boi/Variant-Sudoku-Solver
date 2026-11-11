"""PuzzleMadness German Whispers Sudoku — 2025-04-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 3, 0],
        [6, 0, 4, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [5, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 6), (5, 5), (6, 5), (5, 4), (4, 4), (4, 3)])
    puzzle.add_german_whispers([(8, 6), (8, 5), (7, 5), (6, 6), (6, 7)])
    puzzle.add_german_whispers([(8, 1), (7, 2), (7, 1), (6, 0), (6, 1)])
    puzzle.add_german_whispers([(2, 3), (2, 4), (1, 3), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(3, 2), (3, 1), (3, 0), (2, 1)])
    puzzle.add_german_whispers([(4, 6), (4, 7), (5, 7), (4, 8)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 7), (2, 8)])
    puzzle.add_german_whispers([(7, 7), (6, 8), (5, 8)])
    puzzle.add_german_whispers([(8, 4), (8, 3), (7, 4)])

    return puzzle
