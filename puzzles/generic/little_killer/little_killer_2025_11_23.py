"""PuzzleMadness Little Killer Sudoku — 2025-11-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 3, 0, 7, 0, 0, 0, 0, 0],
        [7, 0, 0, 3, 9, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 5, 0, 0, 0],
        [8, 0, 3, 0, 0, 0, 0, 0, 0],
        [2, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 4, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 16, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 9, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 10, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 15, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 37, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 44, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 29, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 42, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(8, 7), (7, 8)], 14, clue_position=(0, 6, 2))

    return puzzle
