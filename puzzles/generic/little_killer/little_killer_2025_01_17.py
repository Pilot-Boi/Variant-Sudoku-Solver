"""PuzzleMadness Little Killer Sudoku — 2025-01-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 9, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 9, 4, 0, 0, 0, 8, 0],
        [0, 3, 7, 0, 1, 0, 0, 0, 0],
        [5, 6, 0, 0, 9, 0, 0, 4, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 28, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 13, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 37, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 41, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 16, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 7, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 25, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 41, clue_position=(1, 7, 2))

    return puzzle
