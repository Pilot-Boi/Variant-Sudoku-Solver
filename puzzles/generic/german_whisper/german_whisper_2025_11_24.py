"""PuzzleMadness German Whispers Sudoku — 2025-11-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 5, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 5), (5, 4), (6, 3), (6, 2), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(7, 5), (6, 5), (6, 6), (5, 6), (6, 7)])
    puzzle.add_german_whispers([(8, 1), (8, 2), (8, 3), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(3, 6), (2, 5), (2, 4), (3, 4), (2, 3)])
    puzzle.add_german_whispers([(2, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(2, 6), (1, 5), (1, 6), (1, 7)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (0, 0), (1, 1)])
    puzzle.add_german_whispers([(5, 1), (5, 0), (4, 1)])
    puzzle.add_german_whispers([(3, 0), (3, 1), (4, 2)])
    puzzle.add_german_whispers([(5, 8), (4, 8), (3, 7)])

    return puzzle
