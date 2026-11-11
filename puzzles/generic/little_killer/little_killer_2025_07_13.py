"""PuzzleMadness Little Killer Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 9, 2],
        [0, 0, 1, 0, 4, 7, 0, 0, 0],
        [0, 0, 0, 0, 2, 9, 0, 6, 0],
        [7, 0, 0, 0, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 21, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 34, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 37, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 12, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 27, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 36, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 48, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 29, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 19, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 42, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 42, clue_position=(1, 6, 3))

    return puzzle
