"""PuzzleMadness German Whispers Sudoku — 2025-05-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 8, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 4), (3, 5), (4, 6), (4, 7), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)])
    puzzle.add_german_whispers([(8, 2), (7, 3), (8, 4), (7, 4), (6, 5)])
    puzzle.add_german_whispers([(3, 1), (4, 2), (5, 2), (6, 2), (5, 3)])
    puzzle.add_german_whispers([(3, 3), (3, 4), (2, 5), (1, 4)])
    puzzle.add_german_whispers([(8, 5), (8, 6), (7, 7), (8, 7)])
    puzzle.add_german_whispers([(6, 1), (6, 0), (5, 0), (4, 1)])
    puzzle.add_german_whispers([(2, 0), (1, 1), (1, 0)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (8, 0)])
    puzzle.add_german_whispers([(0, 7), (1, 7), (2, 6)])

    return puzzle
