"""PuzzleMadness German Whispers Sudoku — 2025-12-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 2, 0, 0, 0, 0, 0, 0, 6],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 5), (1, 4), (0, 3), (1, 3), (2, 4), (3, 4)])
    puzzle.add_german_whispers([(3, 3), (4, 4), (5, 4), (5, 5), (6, 5)])
    puzzle.add_german_whispers([(6, 8), (5, 8), (5, 7), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(4, 1), (4, 2), (3, 1), (3, 0), (4, 0)])
    puzzle.add_german_whispers([(7, 7), (8, 6), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (2, 6), (1, 6)])
    puzzle.add_german_whispers([(8, 1), (7, 0), (7, 1), (8, 2)])
    puzzle.add_german_whispers([(6, 1), (6, 2), (6, 3)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (0, 1)])

    return puzzle
