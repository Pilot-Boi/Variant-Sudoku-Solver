"""PuzzleMadness German Whispers Sudoku — 2025-10-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 2, 0, 3, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 9, 0, 0, 8],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 4), (7, 5), (7, 4), (8, 3), (7, 2), (6, 2)])
    puzzle.add_german_whispers([(3, 3), (4, 4), (4, 3), (5, 4), (4, 5)])
    puzzle.add_german_whispers([(0, 4), (1, 3), (1, 2), (0, 1), (1, 0)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (7, 7), (6, 7), (5, 6)])
    puzzle.add_german_whispers([(5, 1), (5, 0), (4, 1), (3, 0)])
    puzzle.add_german_whispers([(1, 8), (2, 7), (3, 6), (4, 6)])
    puzzle.add_german_whispers([(2, 5), (1, 5), (0, 6), (1, 7)])
    puzzle.add_german_whispers([(4, 2), (3, 1), (3, 2), (2, 2)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (5, 8)])
    puzzle.add_german_whispers([(8, 1), (7, 0), (7, 1)])

    return puzzle
