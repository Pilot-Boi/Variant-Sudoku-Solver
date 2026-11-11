"""PuzzleMadness Little Killer Sudoku — 2025-08-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 1, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 1, 0, 0, 0, 0],
        [2, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 1, 0, 0, 2],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 0, 0, 4, 0, 1, 0, 0],
        [0, 2, 0, 0, 7, 8, 0, 9, 0],
        [8, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 19, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 21, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 16, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 34, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 36, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 46, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 18, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 36, clue_position=(0, 1, 2))

    return puzzle
