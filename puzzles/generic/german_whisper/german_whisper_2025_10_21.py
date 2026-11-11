"""PuzzleMadness German Whispers Sudoku — 2025-10-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 7, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 6), (7, 5), (6, 6), (5, 7), (5, 8), (6, 7)])
    puzzle.add_german_whispers([(6, 2), (5, 2), (5, 1), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(1, 8), (1, 7), (2, 6), (1, 5), (0, 5)])
    puzzle.add_german_whispers([(3, 2), (3, 1), (4, 2), (3, 3), (2, 4)])
    puzzle.add_german_whispers([(7, 4), (6, 3), (5, 4), (4, 4), (4, 5)])
    puzzle.add_german_whispers([(4, 8), (3, 7), (3, 6), (4, 7)])
    puzzle.add_german_whispers([(8, 2), (8, 1), (7, 0), (8, 0)])
    puzzle.add_german_whispers([(1, 3), (1, 2), (0, 2), (0, 1)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (2, 1)])
    puzzle.add_german_whispers([(4, 6), (5, 5), (6, 4)])
    puzzle.add_german_whispers([(7, 8), (8, 8), (7, 7)])

    return puzzle
