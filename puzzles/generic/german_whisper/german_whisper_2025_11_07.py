"""PuzzleMadness German Whispers Sudoku — 2025-11-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 4, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 5), (6, 4), (7, 5), (8, 4), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(4, 6), (5, 6), (6, 5), (7, 6), (8, 6)])
    puzzle.add_german_whispers([(3, 8), (2, 7), (1, 8), (0, 8), (0, 7)])
    puzzle.add_german_whispers([(2, 4), (3, 3), (3, 2), (4, 2), (5, 2)])
    puzzle.add_german_whispers([(1, 5), (0, 4), (0, 5), (0, 6)])
    puzzle.add_german_whispers([(1, 4), (1, 3), (2, 2), (1, 2)])
    puzzle.add_german_whispers([(1, 1), (2, 0), (3, 0), (4, 1)])
    puzzle.add_german_whispers([(6, 7), (7, 7), (6, 8)])
    puzzle.add_german_whispers([(4, 3), (5, 3), (6, 3)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (7, 0)])
    puzzle.add_german_whispers([(5, 8), (4, 7), (5, 7)])

    return puzzle
