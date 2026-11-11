"""PuzzleMadness Little Killer Sudoku — 2025-07-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 1],
        [7, 0, 0, 0, 5, 0, 0, 0, 4],
        [0, 4, 6, 0, 0, 0, 5, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 9, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 2, 6, 0, 0, 0],
        [0, 0, 0, 0, 1, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 44, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 36, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 21, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 14, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 14, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 16, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 12, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 26, clue_position=(0, 2, 0))

    return puzzle
