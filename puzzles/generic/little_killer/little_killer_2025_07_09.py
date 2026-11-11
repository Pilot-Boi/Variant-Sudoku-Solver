"""PuzzleMadness Little Killer Sudoku — 2025-07-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 4, 9, 1, 0, 0, 0, 5, 0],
        [0, 0, 6, 7, 0, 8, 0, 1, 0],
        [0, 0, 7, 3, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 9, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 21, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 40, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 30, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 26, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 19, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 15, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 30, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 31, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 33, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 9, clue_position=(1, 2, 1))

    return puzzle
