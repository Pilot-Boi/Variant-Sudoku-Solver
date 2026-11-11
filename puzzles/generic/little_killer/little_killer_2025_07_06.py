"""PuzzleMadness Little Killer Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 3, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 7, 0, 0, 0, 8],
        [0, 1, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 6, 1, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 1), (7, 0)], 10, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 20, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 36, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 7, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 35, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 20, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 18, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 43, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 46, clue_position=(1, 9, 2))

    return puzzle
