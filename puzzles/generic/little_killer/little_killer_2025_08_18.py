"""PuzzleMadness Little Killer Sudoku — 2025-08-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 1, 2, 0, 0, 9],
        [0, 0, 8, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 1],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 8, 0, 0],
        [0, 8, 0, 0, 0, 6, 0, 0, 3],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 21, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 12, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 7), (1, 8)], 15, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 39, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 44, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 24, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 23, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 7, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 47, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 35, clue_position=(1, 7, 2))

    return puzzle
