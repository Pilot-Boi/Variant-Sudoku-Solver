"""PuzzleMadness Little Killer Sudoku — 2025-02-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 9, 2, 0, 0, 0, 4, 7],
        [2, 5, 0, 8, 0, 0, 0, 3, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 5, 0, 0, 2, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 3, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 8],
        [0, 0, 0, 0, 3, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 26, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 34, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 21, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 16, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 24, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 34, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 16, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 15, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 42, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 45, clue_position=(0, 0, 2))

    return puzzle
