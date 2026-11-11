"""PuzzleMadness Little Killer Sudoku — 2025-04-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 3],
        [0, 0, 9, 0, 0, 0, 0, 5, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 9, 3, 0],
        [0, 0, 0, 5, 0, 4, 0, 0, 0],
        [0, 9, 2, 0, 6, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 27, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 13, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 47, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 32, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 28, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 24, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 34, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 59, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 16, clue_position=(0, 4, 1))

    return puzzle
