"""PuzzleMadness German Whispers Sudoku — 2025-04-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 4, 8, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 0), (2, 1), (3, 2), (4, 2), (3, 1), (4, 0)])
    puzzle.add_german_whispers([(8, 7), (8, 6), (8, 5), (7, 5), (7, 6)])
    puzzle.add_german_whispers([(3, 6), (4, 7), (5, 7), (6, 7), (6, 8)])
    puzzle.add_german_whispers([(2, 2), (1, 2), (2, 3), (3, 3), (4, 3)])
    puzzle.add_german_whispers([(2, 4), (1, 4), (1, 5), (1, 6), (0, 6)])
    puzzle.add_german_whispers([(6, 0), (7, 1), (8, 2), (8, 1)])
    puzzle.add_german_whispers([(3, 8), (2, 7), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(7, 3), (6, 2), (6, 3), (5, 3)])
    puzzle.add_german_whispers([(4, 6), (5, 6), (5, 5), (4, 4)])

    return puzzle
