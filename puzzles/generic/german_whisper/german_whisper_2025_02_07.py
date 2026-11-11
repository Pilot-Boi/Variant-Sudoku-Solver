"""PuzzleMadness German Whispers Sudoku — 2025-02-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 0, 7],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 3), (4, 2), (3, 1), (4, 1), (5, 2), (6, 3)])
    puzzle.add_german_whispers([(7, 1), (7, 2), (6, 2), (6, 1), (5, 1)])
    puzzle.add_german_whispers([(2, 4), (3, 4), (2, 5), (1, 4), (1, 5)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (4, 7), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(6, 4), (6, 5), (7, 6), (8, 6)])
    puzzle.add_german_whispers([(2, 6), (1, 7), (1, 8), (2, 8)])
    puzzle.add_german_whispers([(4, 4), (3, 5), (4, 5), (5, 5)])
    puzzle.add_german_whispers([(7, 8), (7, 7), (6, 7), (6, 6)])
    puzzle.add_german_whispers([(0, 2), (1, 1), (1, 2)])

    return puzzle
