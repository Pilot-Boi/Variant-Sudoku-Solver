"""PuzzleMadness Little Killer Sudoku — 2025-04-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 5, 3, 0],
        [0, 0, 0, 7, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 9, 0, 5, 0, 1, 0, 7],
        [0, 4, 0, 0, 0, 0, 0, 6, 2],
        [3, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 50, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 29, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 15, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 14, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 28, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 16, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 32, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 34, clue_position=(1, 6, 2))

    return puzzle
