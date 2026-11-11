"""PuzzleMadness German Whispers Sudoku — 2025-11-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 5, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [8, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 5), (6, 6), (5, 5), (4, 6), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (6, 4), (6, 3), (5, 2)])
    puzzle.add_german_whispers([(0, 5), (1, 5), (1, 4), (2, 5), (3, 6)])
    puzzle.add_german_whispers([(3, 5), (4, 4), (3, 4), (2, 3), (1, 2)])
    puzzle.add_german_whispers([(6, 1), (6, 0), (5, 0), (4, 1)])
    puzzle.add_german_whispers([(1, 6), (2, 6), (2, 7), (2, 8)])
    puzzle.add_german_whispers([(2, 1), (2, 2), (3, 2), (4, 2)])
    puzzle.add_german_whispers([(1, 8), (0, 8), (1, 7)])
    puzzle.add_german_whispers([(4, 8), (5, 8), (6, 8)])
    puzzle.add_german_whispers([(7, 7), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(0, 1), (1, 1), (0, 0)])

    return puzzle
