"""PuzzleMadness Little Killer Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 4, 0, 5, 6, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 4, 0, 0],
        [8, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 1, 0],
        [0, 0, 9, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 6, 0, 5, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 9, 0, 0, 0, 4, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 32, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 31, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 30, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 28, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 19, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 10, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 34, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(1, 8), (0, 7)], 12, clue_position=(1, 2, 1))

    return puzzle
