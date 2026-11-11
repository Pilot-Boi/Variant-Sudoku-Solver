"""PuzzleMadness Little Killer Sudoku — 2025-08-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 2, 4, 5, 0, 1],
        [0, 9, 0, 8, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 2, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 8, 9, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 0), (8, 1)], 14, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 12, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 38, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 22, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 41, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 7, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 26, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 39, clue_position=(0, 0, 1))

    return puzzle
