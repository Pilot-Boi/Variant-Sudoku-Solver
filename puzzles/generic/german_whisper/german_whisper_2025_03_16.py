"""PuzzleMadness German Whispers Sudoku — 2025-03-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 1, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 8), (5, 7), (5, 8), (4, 7), (3, 6), (4, 6)])
    puzzle.add_german_whispers([(0, 6), (0, 7), (1, 8), (1, 7), (2, 8)])
    puzzle.add_german_whispers([(3, 5), (2, 5), (2, 4), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(3, 0), (2, 1), (1, 1), (0, 0), (1, 0)])
    puzzle.add_german_whispers([(7, 2), (8, 1), (7, 1), (6, 2), (5, 3)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (6, 6), (7, 7)])
    puzzle.add_german_whispers([(0, 5), (1, 4), (0, 3), (0, 2)])
    puzzle.add_german_whispers([(6, 3), (6, 4), (7, 5), (7, 4)])
    puzzle.add_german_whispers([(4, 2), (3, 2), (2, 3), (1, 2)])
    puzzle.add_german_whispers([(8, 3), (8, 4), (8, 5)])
    puzzle.add_german_whispers([(3, 4), (4, 5), (5, 5)])

    return puzzle
