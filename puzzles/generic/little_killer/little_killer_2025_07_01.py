"""PuzzleMadness Little Killer Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 2, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 2],
        [0, 0, 3, 2, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 7, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 22, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 22, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 40, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 37, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 38, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 24, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(0, 1), (1, 0)], 4, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 29, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 33, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 36, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 12, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 13, clue_position=(0, 5, 3))

    return puzzle
