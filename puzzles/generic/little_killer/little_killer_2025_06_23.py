"""PuzzleMadness Little Killer Sudoku — 2025-06-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 7, 0, 9, 0, 0, 3, 0],
        [0, 0, 2, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 7, 2],
        [0, 0, 0, 0, 5, 0, 0, 2, 7],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 32, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 41, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 13, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 32, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 16, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 35, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 30, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 16, clue_position=(1, 4, 2))

    return puzzle
