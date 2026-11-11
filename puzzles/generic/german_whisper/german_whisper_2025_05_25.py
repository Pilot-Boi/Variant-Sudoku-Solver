"""PuzzleMadness German Whispers Sudoku — 2025-05-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 6), (2, 5), (1, 6), (1, 5), (2, 4), (1, 4)])
    puzzle.add_german_whispers([(5, 0), (6, 0), (7, 1), (8, 0), (7, 0)])
    puzzle.add_german_whispers([(5, 2), (6, 1), (6, 2), (5, 3), (4, 4)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 0), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(6, 8), (6, 7), (7, 6), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(8, 4), (7, 4), (7, 3), (6, 4)])
    puzzle.add_german_whispers([(5, 7), (5, 8), (4, 8), (3, 7)])
    puzzle.add_german_whispers([(4, 5), (4, 6), (3, 5), (3, 6)])
    puzzle.add_german_whispers([(3, 3), (2, 3), (3, 2)])

    return puzzle
