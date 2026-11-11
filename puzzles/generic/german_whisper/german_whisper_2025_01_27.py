"""PuzzleMadness German Whispers Sudoku — 2025-01-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 5, 6],
        [0, 4, 0, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 1, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 2), (3, 1), (4, 1), (5, 2), (4, 3), (4, 4)])
    puzzle.add_german_whispers([(7, 7), (8, 7), (8, 6), (7, 5), (8, 4)])
    puzzle.add_german_whispers([(3, 6), (2, 5), (3, 5), (3, 4), (2, 4)])
    puzzle.add_german_whispers([(2, 6), (1, 5), (0, 6), (0, 7), (1, 6)])
    puzzle.add_german_whispers([(3, 7), (4, 7), (5, 8), (5, 7)])
    puzzle.add_german_whispers([(7, 1), (7, 2), (7, 3), (6, 4)])
    puzzle.add_german_whispers([(6, 2), (5, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (1, 1), (0, 2)])
    puzzle.add_german_whispers([(4, 5), (5, 6), (6, 7)])

    return puzzle
