"""PuzzleMadness German Whispers Sudoku — 2025-03-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 8, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 5), (0, 6), (1, 6), (2, 7), (3, 7), (3, 8)])
    puzzle.add_german_whispers([(8, 1), (7, 0), (7, 1), (8, 2), (7, 3)])
    puzzle.add_german_whispers([(6, 4), (6, 5), (7, 4), (7, 5), (7, 6)])
    puzzle.add_german_whispers([(5, 6), (4, 5), (5, 4), (5, 5), (6, 6)])
    puzzle.add_german_whispers([(5, 3), (4, 3), (3, 2), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(2, 4), (1, 3), (2, 3), (1, 2)])
    puzzle.add_german_whispers([(7, 7), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(1, 7), (2, 8), (1, 8)])
    puzzle.add_german_whispers([(4, 6), (4, 7), (3, 6)])
    puzzle.add_german_whispers([(5, 0), (5, 1), (6, 1)])

    return puzzle
