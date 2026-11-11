"""PuzzleMadness Little Killer Sudoku — 2025-05-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [1, 4, 3, 0, 0, 5, 2, 0, 6],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 8],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 7, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 8), (0, 7)], 16, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 14, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 46, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 35, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 9, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 28, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 31, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 29, clue_position=(1, 4, 2))

    return puzzle
